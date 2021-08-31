from datetime import date, datetime
import os

class Empresa:
    def __init__(self, id,ruc,direccion, tlfn, rS):
        self.id= id
        self.ruc= ruc
        self.direccion=direccion
        self.telefono= tlfn
        self.razonSocial=rS
        self.empleado= Empleado(id,nombre)
        self.departamento= Departamento(id,descripcion)

    def mostrarEmpresa(self):
        print("Empresa: {:17} Id: {}, Ruc: {}, Telefono: {} Dirección: {}".format(self.razonSocial, self.id,self.ruc,self.direccion))
        self.empleado.mostrarEmpleado()
        self.departamento.mostrarDepartamento()

class Departamento:
    def __init__(self, id, descripcion):
        self.id=id
        self.empleado= Empleado
        self.descripcion= descripcion
    
    def mostrarDepartamento(self):
        print("Id: {:5} Descripcion: {}, Empleado: {}" .format(self.id, self.descripcion, self.empleado.nombre()))

class Empleado:
    def __init__(self, id, nom, sueldo, tel, fechaIng):
        self.id= id
        self.nombre= nom
        self.sueldo= sueldo
        self.telefono= tel
        self.fechaIngreso= fechaIng

    def mostrarEmpleado(self):
        return "Empleado: {:5} ID: #{}, Telefono: {}, Sueldo: {}, Fecha de Ingreso: {}".format(self.nombre, self.id, self.telefono, self.sueldo, self.fechaIngreso)

class EmpleadoObrero(Empleado):
    def __init__(self,ced, nom, dir, tel, cont, tipoTrab):
        super().__init__(ced, nom, dir, tel, cont)
        self.oficio= tipoTrab

class EmpleadoOficina(Empleado):
    def __init__(self,id,nom,sueldo,tel,fechaIng, comision= True):
        super().__init__(id,nom,sueldo,tel,fechaIng)
        self.__comision=comision
 
    @property
    def comision(self):
        if self.__comision==True:
            return "El empleado gana la comision el 5%"

    @comision.setter
    def co(self,value):
        if value:
            self.__comision= value
        else:
            self.__comision= "Sin comisión"

    def mostrarEmpleado(self):
        return "Empleado Oficina: {:5} Id: {}, Comisión: {}%".format(self.nombre, self.id, self.__comision)

id= int(input("Ingrese el id de la empresa: "))
ruc= int(input("Ingrese el R.U.C de la empresa: "))
direccion= input("Ingrese la dirección donde se encuentra la empresa: ")
tlfn= int(input("Ingrese el número telefonico de la empresa: "))
razonsocial= input("Ingrese la razón social de la empresa: ")
os.system("cls")
empresa= Empresa(id,ruc,direccion,tlfn,razonsocial)
print(empresa.mostrarEmpresa())
depa=2
while depa==2:
    id1= int(input("Ingrese el Id del departamento de oficina: "))
    descripcion1="Oficina"
    id2= int(input("Ingrese el Id del departamento de Obreros: "))
    descripcion2dc="Obreros"
    empleados= int(input("Cuantos empleados va a ingresar: "))
    for x in range(empleados):
       id= int(input("Ingrese el id que pertenece al empleado {}: #" .format(x)))
       nombre= input("Ingrese el nombre del empleado {}: ".format(x))
       telefono= int(input("Ingrese el número celular del empleado {}: ".format(nombre)))
       sueldo= float(input("Ingrese el sueldo del empleado {}: ".format(nombre)))
       año= int(input("Ingrese el año que ingreso el empleado {}: ".format(nombre)))
       mes= int(input("Ingrese el mes que ingreso el empleado {}: ".format(nombre)))
       dia= int(input("Ingrese el dia que ingreso el empleado {}: ".format(nombre)))
       fechaIngreso= date(año,mes,dia)
       oficio= input("El empleado que cargo tienen [Oficina, Obrero]: ")
       if oficio=="Oficina":
           depa= Departamento(id1,descripcion1)
           print(depa.mostrarDepartamento())
           
emp= Empleado(id,nombre,sueldo,telefono,fechaIngreso)
print(emp.mostrarEmpleado())
comision=float(input("Ingrese la comision que posee el empleado: "))
emp1= EmpleadoOficina(id,nombre,sueldo,telefono,fechaIngreso,comision)
print(emp1.mostrarEmpleado())