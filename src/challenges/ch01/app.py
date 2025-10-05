from __future__ import annotations # use class before it is declared
from abc import ABC, abstractmethod
from dataclasses import dataclass
from tkinter import simpledialog, messagebox
import tkinter as tk

#================= input & output interfaces =============

# input and output 
class IInput(ABC):
  @abstractmethod
  def read(self, prompt: str, lower: bool=True) -> str:
    pass
  
class IOutput(ABC):
  @abstractmethod
  def write(self, text: str) -> None:
    pass

#================= concrete console input and output =============

class ConsoleIn(IInput):
  def read(self, prompt: str, lower: bool=True) -> str:
    response = input(prompt)

    if lower:
      return response.strip().lower()
    
    return response

class ConsoleOut(IOutput):
  def write(self, text: str) -> None:
    print(text)

#================= Tkinter in/out =============

class TkinterIn(IInput):
  def __init__(self, root: tk.Tk):
    # tkinter root/app
    self.root = root

  def read(self, prompt: str, lower: bool=True) -> str:
    """ get input using tkinter """
    response = simpledialog.askstring("Input", prompt=prompt, parent=self.root)

    # check if user return pressed cancel
    if response is None:
      return ''

    return response.strip().lower() if lower else response.strip()

#================= tkinter output =============

class TkinterOut(IOutput):
  def __init__(self, root: tk.Tk) -> None:
    self.root = root
  
  def write(self, text: str) -> None:
    messagebox.showinfo("Output", text, parent=self.root)

#================= multi output -> composite pattern =============

class MultiOut(IOutput):
  """ handle multiple outputs """
  def __init__(self, outputs: list[IOutput]) -> None:
    self.outputs = outputs

  def write(self, text: str) -> None:
    """ print to all outputs """
    for out in self.outputs:
      out.write(text)

#================= validator =============

from enum import Enum

class ValidatorTypes(Enum):
  EMPTY_STR = 'empty_str'
  ALPHA_SPACE = 'alpha_space'

class IValidator(ABC):
  @abstractmethod
  def validate(self, text: str) -> str | None:
    """ validate user input """
    pass

class ValidateEmptyStr(IValidator):
  def validate(self, text: str) -> str | None:
    """ check if string empty -> True """
    if not text:
      # just return the error
      return "Name can't be empty!"

    return None

class ValidateAlphaSpace(IValidator):
  def validate(self, text: str) -> str | None:
    """ check if string contains alphabet and spaces only => return True """
    if not all(ch.isalpha() or ch.isspace() for ch in text):
      return "only alphabets are allowed!"

    return None

#================= validator =============

class ValidatorPipeline: 
  def __init__(self, validators: list[IValidator]):
    # keep a list of validators
    self.validators = validators

  def validate(self, text: str) -> str | None:
    """ return error message or None if valid """
    for v in self.validators:
      err = v.validate(text=text)

      if err:
        return err
    
    # no error
    return None
      
#================= replay strategy =============

class ReplayResult(Enum):
  CONTINUE = 1
  EXIT = 2
  INVALID = 3

class ReplayStrategy(ABC):
  @abstractmethod
  def decide(self, response: str) -> ReplayResult: pass

# different algorithms for responding to user replay input 
class YesNoReplayStrategy(ReplayStrategy):
  def decide(self,response: str) -> ReplayResult:
    if response in {"yes", 'y'}:
      return ReplayResult.CONTINUE
    elif response in {"no", 'n'}:
      return ReplayResult.EXIT
    else:
      return ReplayResult.INVALID

#================= game state patter =============

class GameState(ABC):
  @abstractmethod
  def run(self, context: GameContext) -> None:
    pass

#================= main menu state =============

class MainMenuState(GameState):
  def run(self, context: GameContext) -> None:
    context.outDevice.write("""
    ===================\n
    ==== Main Menu ====
    ===================\n
    """)

    context.outDevice.write("\n 1. New Game \n")
    context.outDevice.write("\n 2. Exit\n")

    option = context.inDevice.read("\nEnter an option: \n")

    if option == '1':
      context.set_state(state=AskNameState())
    elif option == '2':
      context.set_state(state=ExitGameState())
    else:
      context.set_state(state=self)

#================= ask name state =============

class AskNameState(GameState):
  def run(self, context: GameContext) -> None:
    response = context.inDevice.read("Enter your name: \n")

    # validate name
    # check for empty string
    err = context.validator.validate(text=response)

    if err:
      context.outDevice.write(err)
      return # next function call
    
    context.outDevice.write(text=f"👤 your name is: {response}.\n")
    context.outDevice.write(text="thanks for using my program.\n")

    # next state
    context.set_state(AskReplayState())

#================= ask replay state =============

class AskReplayState(GameState):
  def run(self, context: GameContext) -> None:
    """ run ask for replay logic """
    response = context.inDevice.read("Do you want to play again? (yes/no) \n")

    result = context.replay_strategy.decide(response=response)

    if result == ReplayResult.CONTINUE:
      context.outDevice.write(text="Starting a new game...🎮\n")

    elif result == ReplayResult.EXIT: #quit
      context.set_state(state=ExitGameState())
    elif result == ReplayResult.INVALID: # invalid
      context.outDevice.write(text="Invalid input, try again!\n")

#================= exit game state =============

class ExitGameState(GameState):
  def run(self, context: GameContext) -> None:
    context.outDevice.write(text="Goodbye! 😘\n ")
    # set the state to None
    context.set_state(state=None)

#================= main program =============

class GameContext:
  def __init__(
      self, 
      inDevice: IInput, 
      outDevice: IOutput,
      replay_strategy: ReplayStrategy,
      validator: ValidatorPipeline,
      ) -> None:
    self.inDevice = inDevice
    self.outDevice = outDevice
    self.replay_strategy = replay_strategy
    self.validator = validator

    # current state
    self.state = MainMenuState()

  def set_state(self, state: GameState | None) -> None:
    self.state = state

  def start(self):
    """ start the main program """

    while self.state:
      self.state.run(context=self)
      
#================= main program =============

def main():
  try:

    # thinker
    root = tk.Tk()
    root.withdraw()

    inDevice = ConsoleIn()
    outDevice = MultiOut(outputs=[ConsoleOut(), TkinterOut(root=root)])

    validator = ValidatorPipeline(validators=[ValidateEmptyStr(), ValidateAlphaSpace()])

    replay_strategy = YesNoReplayStrategy()
    program = GameContext(
      inDevice=inDevice, 
      outDevice=outDevice,
      replay_strategy=replay_strategy,
      validator=validator,
    )

    program.start()
  except Exception as e:
    print("main(): failed\n\n", e)

main()