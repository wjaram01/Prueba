from datetime import *
import os


class Empresa:

    def __init__(self, nombreEmpresa, direccion, telefono, razonSocial, ruc):
        self.nombre = nombreEmpresa
        self.departamento = []
        self.direccion = direccion
        self.telefono = telefono
        self.razonSocial = razonSocial
        self.ruc = ruc

    def MostrarEmpresa(self):
        print("""
        Nombre empresa: {}
        Direccion:      {}
        Telefono:       {}
        Razon Social:   {}
        ruc:            {}""".format(self.nombre, self.direccion, self.telefono, self.razonSocial, self.ruc))

    def CrearDepartamento(self, descripcion):
        # desc = input("Ingrese una descripcion del departamento {}: ".format(i+1))
        objDep = Departamento(descripcion)
        self.departamento.append(objDep)


class Departamento:
    id = 0

    def __init__(self, descripcion):
        Departamento.id += 1
        self.__id = Departamento.id
        self.empleados = []
        self.descripcion = descripcion

    def MostrarDepartamentos(self):
        print("Departamento de {}".format(self.descripcion))

    def CrearEmpleados(self):
        # emp = input("Ingrese cuantos empleados desea agregar: ")
        emp = '1'
        for z in range(int(emp)):
            while True:
                opc = input("Seleccione Obrero(1) - Oficinista(0)")
                if opc in ("0", "1"):
                    break
                else:
                    pass
                os.system("cls")
            if opc == "1":
                value = ['Walter Jara ', '1729761302', 200, [20, 5, 2020], 'Av.Mariscal Sucre']
                # datos = ["nombre", "cedula", "sueldo", "fechaIngreso", "direccion"]
                # for j in datos:
                #     aux = input("Ingrese el {}: ".format(j))
                #     value.append(aux)
                aux3 = value[3]
                objObrero = Obrero(value[0], value[1], value[2], date(aux3[2], aux3[1], aux3[0]), value[4],
                                   sindicato=True, contratoColectivo=True)
                self.empleados.append(objObrero)
            else:
                value = ['Johanna Moreno', '093673536', 400, [25, 8, 2020], 'Rocafuerte']
                # datos = ["nombre", "cedula", "sueldo", "fechaIngreso", "direccion"]
                # for j in datos:
                #     aux = input("Ingrese el {}: ".format(j))
                #     value.append(aux)
                aux3 = value[3]
                objAdministrativo = Administrativo(value[0], value[1], value[2], date(aux3[2], aux3[1], aux3[0]),
                                                   value[4], comision=True)
                self.empleados.append(objAdministrativo)

    def MostrarEmpleados(self):
        print("**********DEPARTAMENTO DE {}************".format(self.descripcion))
        for i, v in enumerate(self.empleados):
            print("{}.{}".format(i, v.nombre))


class Empleado:
    id = 0

    def __init__(self, nombre, cedula, sueldo, fechaIngreso, direccion):
        Empleado.id += 1
        self.nombre = nombre
        self.cedula = cedula
        self.sueldo = sueldo
        self.ingreso = fechaIngreso
        self.direccion = direccion

    def MostrarEmpleado(self):
        print("""-----------------------EMPLEADO---------------------------
         ID Empleado:    {}
         Nombres:        {}
         Cedula          {}
         Sueldo:         {}
         Fecha Ingreso:  {}
         Direccion:      {}""".format(Empleado.id, self.nombre, self.cedula, self.sueldo,
                                      self.ingreso, self.direccion))


class Obrero(Empleado):
    def __init__(self, nombre, cedula, sueldo, FechaIngreso, direccion, sindicato, contratoColectivo):
        super().__init__(nombre, cedula, sueldo, FechaIngreso, direccion)
        self.sindicato = sindicato
        self.contrato = contratoColectivo

    def MostrarEmpleado(self):
        super().MostrarEmpleado()
        print("""         Tipo Empleado:  {}
         Sindicato:      {}
         Cont.Colectivo: {}""".format("Obrero", self.sindicato, self.contrato))


class Administrativo(Empleado):
    def __init__(self, nombre, cedula, sueldo, FechaIngreso, direccion, comision):
        super().__init__(nombre, cedula, sueldo, FechaIngreso, direccion)
        self.comision = comision

    def MostrarEmpleado(self):
        print(Empleado.id)
        super().MostrarEmpleado()
        print("""         TipoEmpleado:   {}
         Comision:       {}""".format("Administrativo", self.comision))


class Prestamo:
    id = 0

    def __init__(self, cuota, fecha, valor, numPagos, empleado, saldo, estado):
        Prestamo.id += 1
        self.__id = Prestamo.id
        self.cuota = cuota
        self.fecha = fecha
        self.valor = valor
        self.numPagos = numPagos
        self.empleado = empleado
        self.saldo = saldo
        self.estado = estado

    @property
    def get_id(self):
        return self.__id

    def MostraPrestamo(self):
        print("""
        ID Prestamo:        {}
        Cuota:              {}
        Fecha:              {}
        Valor:              {}
        Numero Pagos:       {}
        Empleado:           {}
        Saldo:              {}
        Estado:             {}""".format(self.get_id, self.cuota, self.fecha, self.valor, self.numPagos,
                                         "Miau", self.saldo, self.estado))


class Sobretiempo:
    id = 0

    def __init__(self, valorhora=0.0, horasRecargo=0, empleado=None, horasExtraordinarias=0, estado=False):
        Sobretiempo.id += 1
        self.__id = Sobretiempo.id
        self.recargo = horasRecargo
        self.extra = horasExtraordinarias
        self.fecha = date.today()
        self.estado = estado
        self.empleado = empleado
        self.sobretiempo = 0
        self.valorhora = valorhora

    @property
    def get_id(self):
        return self.__id

    def CalcularSobretiempo(self):
        vsobretiempo = self.valorhora * (self.recargo * 0.50 + self.extra * 2)
        self.sobretiempo = vsobretiempo

    def MostrarSobretiempo(self):
        print("""************ INFORMACION DE SOBRETIEMPO ****************
        ID Sobretiempo:  {}
        Empleado:        {}
        Hrs Recargo:     {}
        Hrs Extra:       {}
        Valor Sobret:    {}
        Fecha:           {}
        Estado:          {}""".format(self.get_id, self.empleado.nombre, self.recargo, self.extra, self.sobretiempo,
                                      self.fecha, self.estado))


class Deducciones:
    def __init__(self, iess, comision, antiguedad):
        self.iess = iess
        self.comision = comision
        self.antiguedad = antiguedad

    def MostrarDeduccion(self):
        print("""
        iess:       {}
        comision:   {}
        antiguedad: {}""".format(self.iess, self.comision, self.antiguedad))


class Nomina:
    id = 0

    def __init__(self, empleado=None, fecha=None, sueldo=None, sobretiempo=None, comision=None, antiguedad=None
                 , iess=None, prestamo=None):
        Nomina.id += 1
        self.__id = Nomina.id
        self.empleado = empleado
        self.fecha = fecha
        self.sueldo = sueldo
        self.sobretiempo = sobretiempo
        self.comision = comision
        self.antiguedad = antiguedad
        self.toting = 0
        self.iess = iess
        self.prestamo = prestamo
        self.totDes = 0
        self.liquidoRecibir = 0

    def MostrarNomina(self):
        idNomina = self.__id
        comisionEmpOficina = self.comision * self.sueldo
        anti_year = round((date.today() - self.empleado.ingreso).days/365, 0)
        antiguedadEmpObrero = (self.antiguedad * anti_year) * self.sueldo
        iessEmpleado = round(self.iess * (self.sueldo + self.sobretiempo), 2)
        prestamoEmpleado = self.prestamo.cuota
        toting = self.sueldo + self.sobretiempo + comisionEmpOficina + antiguedadEmpObrero
        totdes = iessEmpleado + prestamoEmpleado
        liquidoRecibir = round(toting - totdes, 2)
        Nomina.CabNomina(self)
        print("""
           {}         {}        {}        {}           {}            {}           {}             {}        {}          {}            {}""".format(
            idNomina, self.empleado.nombre, self.fecha, self.empleado.sueldo, self.sobretiempo,
            comisionEmpOficina, antiguedadEmpObrero, toting, iessEmpleado, totdes, liquidoRecibir))

    def CabNomina(self):
        print("************Nomina***************")
        print()
        print("""
        idNomina        Empleado             Fecha         Sueldo       Sobretiempo      Comision     Antiguedad    Tot. Ingreso     iess       TotDescuento          Liquido""")


empresa1 = Empresa(nombreEmpresa="baratodo", direccion="Miau", telefono="0987262", razonSocial="Market", ruc="0283363")
empresa1.MostrarEmpresa()
input("Presione la tecla ENTER para continuar...")
os.system('cls')
empresa1.CrearDepartamento("Economia")
departamento = empresa1.departamento
departamento = departamento[0]
departamento.MostrarDepartamentos()
input("Presione la tecla ENTER para continuar...")
os.system('cls')
departamento.CrearEmpleados()
empleados = departamento.empleados
empleados = empleados[0]
empleados.MostrarEmpleado()
input("Presione la tecla ENTER para continuar...")
os.system('cls')
objDeducc = Deducciones(0.0945, 0.05, 0.02)
objDeducc.MostrarDeduccion()
objSobret = Sobretiempo(4.50, 40, empleados, 10, False)
objSobret.CalcularSobretiempo()
objSobret.MostrarSobretiempo()
input("Presione la tecla ENTER para continuar...")
os.system('cls')
objPrestamo = Prestamo(100, date.today(), 1000, 10, empleados, 1000, False)
objNomina = Nomina(empleados, date.today(), empleados.sueldo, objSobret.sobretiempo, objDeducc.comision, objDeducc.antiguedad, objDeducc.iess, objPrestamo)
objNomina.MostrarNomina()
input("Presione la tecla ENTER para continuar...")
os.system('cls')