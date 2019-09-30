import clr

clr.AddReference("System.Windows.Forms")

from System.Drawing import Size, Point
import System.Windows.Forms as WinForms


class HelloForm(WinForms.Form):

    def __init__(self):
        self.textBox1 = WinForms.TextBox()
        self.button1 = WinForms.Button()
        self.SuspendLayout()

        # textBox1
        self.textBox1.Location = Point(156, 48)
        self.textBox1.Name = "textBox1"
        self.textBox1.Size = Size(290, 21)
        self.textBox1.TabIndex = 0
        self.textBox1.Text = "Helllo World"

        # button1
        self.button1.Location = Point(156, 140)
        self.button1.Name = "button1"
        self.button1.Size = Size(147, 23)
        self.button1.TabIndex = 1
        self.button1.Text = "Click Me"
        self.button1.UseVisualStyleBackColor = True
        self.button1.Click += self.button_Click

        # Form1
        self.AutoScaleMode = WinForms.AutoScaleMode.Font
        self.ClientSize = Size(709, 354)
        self.Controls.Add(self.button1)
        self.Controls.Add(self.textBox1)
        self.Name = "Form1"
        self.Text = "Form1"
        self.ResumeLayout(False)
        self.PerformLayout()        

    def button_Click(self, sender, args):
        """Button click event handler"""
        print("Click")
        WinForms.MessageBox.Show("Hello, there.")


def main():
    form = HelloForm()
    app = WinForms.Application

    app.Run(form)


if __name__ == '__main__':
    main()
