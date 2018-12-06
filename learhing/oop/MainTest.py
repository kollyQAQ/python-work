from learhing.oop import Student

class Demo:
    def test(self):
        bart = Student.Student('Bart Simpson', 59)
        bart.print_score()
        bart.set_score(11)
        bart.print_score()

if __name__ == '__main__':
    demo = Demo()
    demo.test()
