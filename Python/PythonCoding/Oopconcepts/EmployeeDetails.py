class EmployeeDetails:
    def __init__(self, empno, ename, basic_pay):
        self.__empno = empno
        self.__empname = ename
        self.__basic_pay = basic_pay
        self.__da = 20.0
        self.__hra = 10.0
        self.__pf = 5.5

    # empno property
    @property
    def empno(self):
        return self.__empno

    @empno.setter
    def empno(self, eno):
        self.__empno = eno

    # empname property
    @property
    def ename(self):
        return self.__empname

    @ename.setter
    def ename(self, en):
        self.__empname = en

    # basic_pay property
    @property
    def basic_pay(self):
        return self.__basic_pay

    @basic_pay.setter
    def basic_pay(self, pay):
        self.__basic_pay = pay

    # internal calculations
    def _calculate_allowance(self):
        return (self.__basic_pay * self.__da / 100) + (self.__basic_pay * self.__hra / 100)

    def _calculate_deduction(self):
        return self.__basic_pay * self.__pf / 100

    def calculate_netsal(self):
        return self.__basic_pay + self._calculate_allowance() - self._calculate_deduction()


