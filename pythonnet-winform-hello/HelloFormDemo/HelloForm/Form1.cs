using System;
using System.Windows.Forms;

namespace WindowsFormsAppTemporaryTest {
    public partial class Form1 : Form {
        public Form1() {
            InitializeComponent();
        }

        private void Button1_Click(object sender, EventArgs e) {
            MessageBox.Show("Hello, there!");
        }
    }
}
