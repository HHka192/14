
from kivy.app import App
from kivy.lang import Builder


Builder.load_string('''
<LinePlayground>:
    canvas:
        Color:
            rgba: .4, .4, 1, root.alpha
        Line:
            points: self.points
            joint: self.joint
            cap: self.cap
            width: self.line-width
            close: self.close
            dash_length: self.dash_length
            dash_offset: self.dash_offset
            dashes: self.dashes
        Color:
            rgba: .8, .8, .8, root.alpha_controlline
        Line:
            points: self.points
            close: self.close
            dash_length: self.dash_length
            dash_offset: self.dash_offset
            dashes: self.dashes
        Color:
            rgba: 1, .4, .4, root.alpha
        Line:
            points: self.points2
            joint: self.joint
            cap: self.cap
            width: self.linewidth
            close: self.close
            dash_length: self.dash_length
            dash_offset: self.dash_offset
            dashes: self.dashes

    GridLayout:
        cols: 2
        size_hint: 1, None
        height: 44 * 5

        GridLayout:
            cols: 2

            Label:
                text: 'Alpha'
            Slider:
                value: root.alpha
                on_value: root.alpha = float(args[1])
                min: 0.
                max: 1.
            Label:
                text: 'Alpha Control Line'
            Slider:
                value: root.alpha_controlline
                on_value: root.alpha_controlline = float(args[1])
                min: 0.
                max: 1.
            Label:
                text: 'Width'
            Slider:
                value: root.linewidth
                on_value: root.linewidth = args[1]
                min: 1
                max: 40
            Label:
                text: 'Cap'
            GridLayout:
                rows: 1
                ToggleButton:
                    group: 'cap'
                    text: 'none'
                    on_press: root.cap = self.text
                ToggleButton:
                    group: 'cap'
                    text: 'round'
                    on_press: root.cap = self.text
                ToggleButton:
                    group: 'cap'
                    text: 'square'
                    on_press: root.cap = self.text
            Label:
                text: 'Joint'
            GridLayout:
                rows: 1
                ToggleButton:
                    group: 'joint'
                    text: 'none'
                    on_press: root.joint = self.text
                ToggleButton:
                    group: 'joint'
                    text: 'round'
                    on_press: root.joint = self.text
                ToggleButton:
                    group: 'joint'
                    text: 'miter'
                    on_press: root.joint = self.text
                ToggleButton:
                    group: 'joint'
                    text: 'bevel'
                    on_press: root.joint = self.text

            Label:
                text: 'Close'
            ToggleButton:
                text: 'Close line'
                on_press: root.close = self.state == 'down'

            Label:
                text: 'Dashes'
            GridLayout:
                rows: 1
                ToggleButton:
                    group: 'dashes'
                    text: 'none'
                    state: 'down'
                    allow_no_selection: False
                    size_hint_x: None
                    width: self.texture_size[0]
                    padding_x: '5dp'
                    on_state:
                        if self.state == 'down': root.dashes = []
                        if self.state == 'down': root.dash_length = 1
                        if self.state == 'down': root.dash_offset = 0
                ToggleButton:
                    id: constant
                    group: 'dashes'
                    text: 'Constant: '
                    allow_no_selection: False
                    size_hint_x: None
                    width: self.texture_size[0]
                    padding_x: '5dp'
                    on_state:
                        if self.state == 'down': root.dashes = []
                        if self.state == 'down': root.dash_length = \
                            int(dash_len.text or 1)
                        if self.state == 'down': root.dash_offset = \
                            int(dash_offset.text or 0)
                Label:
                    text: 'len'
                    size_hint_x: None
                    width: self.texture_size[0]
                    padding_x: '5dp'
                TextInput:
                    id: dash_len
                    size_hint_x: None
                    width: '30dp'
                    input_filter: 'int'
                    multiline: False
                    text: '1'
                    on_text: if constant.state == 'down': \
                        root.dash_length = int(self.text or 1)
                Label:
                    text: 'offset'
                    size_hint_x: None
                    width: self.texture_size[0]
                    padding_x: '5dp'
                TextInput:
                    id: dash_offset
                    size_hint_x: None
                    width: '30dp'
                    input_filter: 'int'
                    multiline: False
                    text: '0'
                    on_text: if constant.state == 'down': \
                        root.dash_offset = int(self.text or 0)
                ToggleButton:
                    id: dash_list
                    group: 'dashes'
                    text: 'List: '
                    allow_no_selection: False
                    size_hint_x: None
                    width: self.texture_size[0]
                    padding_x: '5dp'
                    on_state:
                        if self.state == 'down': root.dashes = list(map(lambda\
                            x: int(x or 0), dash_list_in.text.split(',')))
                        if self.state == 'down': root.dash_length = 1
                        if self.state == 'down': root.dash_offset = 0
                TextInput:
                    id: dash_list_in
                    size_hint_x: None
                    width: '180dp'
                    multiline: False
                    text: '4,3,10,15'
                    on_text: if dash_list.state == 'down': root.dashes = \
                        list(map(lambda x: int(x or 0), self.text.split(',')))

        AnchorLayout:
            GridLayout:
                cols: 1
                size_hint: None, None
                size: self.minimum_size
                ToggleButton:
                    size_hint: None, None
                    size: 100, 44
                    text: 'Animate'
                    on_state: root.animate(self.state == 'down')
                Button:
                    size_hint: None, None
                    size: 100, 44
                    text: 'Clear'
                    on_press: root.points = root.points2 = []

''')

class TutorialApp(App):

    _update_points_animation_ev = None


import math
import turtle

def xt(t):
    return 16 * math.sin(t) ** 3

def yt(t):
    return 13 * math.cos(t) - 5 * \
                math.cos(2 * t ) - 2 * \
                math.cos(3 * t) - \
                math.cos(4 * t)
t= turtle.Turtle()
t.speed(1000)
turtle.colormode(255)
turtle.Screen().bgcolor(0, 0, 0)
for i in range(2550):
    t.goto((xt(i) * 20 , yt(i) * 20))
    t.pencolor((255-i) % 255, i % 255, (255 + i )// 2 % 255 )
    t.goto(0, 0)

t.hideturtle()
turtle.update()
turtle.mainloop()

t.hideturtle()
turtle.update()
turtle.mainloop()


class LinePlayground:
    pass


def TestLineApp():
    pass


if __name__ == '__main__':
    TestLineApp().run(None)
