from app import App
from app_components import clear_background

from events.input import Buttons, BUTTON_TYPES

class DemoApp(App):
  def __init__(self):
    self.button_states = Buttons(self)

  def update(self, delta):
    if self.button_states.get(BUTTON_TYPES["CANCEL"]):
      # The button_states do not update while you are in the background.
      # Calling clear() ensures the next time you open the app, it stays
      # open. Without it the app would close again immediately.
      self.button_states.clear()
      self.minimise()

  def draw(self, ctx):
    clear_background(ctx)
    ctx.text_align = ctx.CENTER
    ctx.text_baseline = ctx.MIDDLE
    ctx.move_to(0, 0).rgb(0.7, 1, 1).text("Hello, world!")

__app_export__ = DemoApp
