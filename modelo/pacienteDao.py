from.conexion import ConexionDB
from tkinter import messagebox

def editarDatoPaciente(persona, idPersona):
    conexion = ConexionDB()
    sql = f"""UPDATE Persona SET nombre = '{persona.nombre}', apellidoPaterno = '{persona.apellidoPaterno}', apellidoMaterno = '{persona.apellidoMaterno}',
        rut = {persona.rut}, fechaNacimiento = '{persona.fechaNacimiento}', edad = {persona.edad}, curso = '{persona.curso}', antecedentes = '{persona.antecedentes}',
        correo = '{persona.correo}', telefono = '{persona.telefono}', activo = 1 WHERE idPersona = {idPersona}"""

    try:
        conexion.cursor.execute(sql)
        conexion.cerrarConexion()
        title = 'EDITAR ESTUDIANTE'
        mensaje = 'Estudiante editado existosamente'
        messagebox.showinfo(title, mensaje)

    except:
        title = 'EDITAR ESTUDIANTE'
        mensaje = 'Error al editar estudiante'
        messagebox.showinfo(title, mensaje)

def guardarDatoPaciente(persona):
    conexion = ConexionDB()
    sql = f"""INSERT INTO Persona (nombre, apellidoPaterno, apellidoMaterno, rut, fechaNacimiento, edad, curso, antecedentes, correo, telefono, activo) VALUES
    ('{persona.nombre}','{persona.apellidoPaterno}','{persona.apellidoMaterno}',{persona.rut},'{persona.fechaNacimiento}',{persona.edad},'{persona.curso}','{persona.antecedentes}','{persona.correo}','{persona.telefono}',1)"""
    try:
        conexion.cursor.execute(sql)
        conexion.cerrarConexion()
        title = 'Registrar Estudiante'
        mensaje = 'Estudiante registrado exitosamente'
        messagebox.showinfo(title, mensaje)
    except:
        title = 'Registrar Estudiante'
        mensaje = 'Error al registrar Estudiante'
        messagebox.showerror(title, mensaje)

def listar():
    conexion = ConexionDB()

    listaPersona = []
    sql = 'SELECT * FROM Persona WHERE activo = 1'

    try:
        conexion.cursor.execute(sql)
        listaPersona = conexion.cursor.fetchall()
        conexion.cerrarConexion()

    except:
        title = 'Datos'
        mensaje = 'Registros no existen'
        messagebox.showwarning(title,mensaje)
    
    return listaPersona

def listarCondicion(where):
        conexion = ConexionDB()
        listaPersona = []
        sql = f'SELECT * FROM Persona {where}'

        try:
            conexion.cursor.execute(sql)
            listaPersona = conexion.cursor.fetchall()
            conexion.cerrarConexion
        except:
            title = 'Datos'
            mensaje = 'Registros no existen'
            messagebox.showwarning(title,mensaje)
        return listaPersona

def eliminarPaciente(idPersona):
        conexion = ConexionDB()
        sql = f"""UPDATE Persona SET activo = 0 WHERE idPersona = {idPersona}"""
        
        try:
            conexion.cursor.execute(sql)
            title = 'Eliminar Estudiante'
            mensaje = 'Estudiante eliminado exitosamente'
            messagebox.showwarning(title,mensaje)
            conexion.cerrarConexion()
        except:
            title = 'Eliminar Paciente'
            mensaje = 'Error'
            messagebox.showwarning(title,mensaje)
 

class Persona:
    def __init__(self, nombre, apellidoPaterno, apellidoMaterno, rut, fechaNacimiento, edad, curso, antecedentes, correo, telefono):
        self.idPersona = None
        self.nombre = nombre
        self.apellidoPaterno = apellidoPaterno
        self.apellidoMaterno = apellidoMaterno
        self.rut = rut
        self.fechaNacimiento = fechaNacimiento
        self.edad = edad
        self.curso = curso
        self.antecedentes = antecedentes
        self.correo = correo
        self.telefono = telefono

    def __str__(self):
        return f'Persona[{self.nombre},{self.apellidoPaterno},{self.apellidoMaterno},{self.rut},{self.fechaNacimiento},{self.edad},{self.curso},{self.antecedentes},{self.correo},{self.telefono}]'