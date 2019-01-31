# JAVA:
# class Person {
#     public static int visited;
#
#     Person(String name, int age, float height) {
#         this.name = name;
#         this.age = age;
#         this.height = height;
#     }
#
#     public String getName() {
#         return name;
#     }
#
#     public int getAge() {
#         return age;
#     }
#
#     public void showInfo() {
#         System.out.println("name:" + name);
#         System.out.println("age:" + age);
#         System.out.println("height:" + height);
#         System.out.println("visited:" + visited);
#         Person.visited ++;
#     }
#
#     private String name;
#     protected int age;
#     public  float height;
# }
#
# class Teacher extends Person {
#
#     Teacher(String name, int age, float height) {
#         super(name, age, height);
#     }
#
#     public String getTitle() {
#         return title;
#     }
#
#     public void setTitle(String title) {
#         this.title = title;
#     }
#
#     public void showInfo() {
#         System.out.println("title:" + title);
#         super.showInfo();
#     }
#
#     private String title;
#
# }
# public class Test {
#     public static void main(String args[]) {
#         Person tony = new Person("Tony", 25, 1.77f);
#         tony.showInfo();
#         System.out.println();
#         Teacher jenny = new Teacher("Jenny", 34, 1.68f);
#         jenny.setTitle("教授");
#         jenny.showInfo();
#     }
# }

####################################################
# Python


class Person:
    visited = 0  # static

    def __init__(self, name, age, height):
        self.__name = name  # private
        self._age = age     # protected
        self.height = height

    def getName(self):
        return self.__name

    def getAge(self):
        return self._age

    def showInfo(self):
        print("name: {}".format(self.__name))
        print("age: {}".format(self._age))
        print("height: {}".format(self.height))
        print("visited: {}".format(self.visited))
        Person.visited += 1


class Teacher(Person):
    def __init__(self, name, age, height):
        super().__init__(name, age, height)
        self.__title = None

    def getTitle(self):
        return self.__title

    def setTitile(self, title):
        self.__title = title

    def showInfo(self):
        print("title: {}".format(self.__title))
        super().showInfo()


def testPerson():
    t = Person("Tony",25,1.77)
    t.showInfo()
    print("====")
    j = Teacher("Jenny",34,1.68)
    j.setTitile("教授")
    j.showInfo()

testPerson()