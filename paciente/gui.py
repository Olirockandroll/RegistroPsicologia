import tkinter as tk
from tkinter import messagebox
from modelo.pacienteDao import Persona, guardarDatoPaciente, listarCondicion, listar, editarDatoPaciente, eliminarPaciente
from tkinter import *
from tkinter import Button, ttk, Toplevel, scrolledtext, LabelFrame
from modelo.historiaMedicaDao import historiaMedica, guardarHistoria, listarHistoria, eliminarHistoria, editarHistoria
import tkcalendar as tc
from tkcalendar import *
from tkcalendar import Calendar
from datetime import datetime, date

class Frame(tk.Frame):
    def __init__(self, root):

        super().__init__(root, width=1280, height=720)
        self.root = root
        self.pack()
        self.config(bg='#F5F5F5')
        self.idPersona = None
        self.idPersonaHistoria = None
        self.idHistoriaMedica =None
        self.idHistoriaMedicaEditar = None
        self.camposPaciente()
        self.deshabilitar()
        self.tablaPaciente()
        

    def camposPaciente(self):

        #LABELS
        self.lblNombre = tk.Label(self, text='Nombre Alumno: ')
        self.lblNombre.config(font=('Arial',10,'bold'), bg='#F5F5F5')
        self.lblNombre.grid(column=0, row=1, padx=10, pady=5, sticky='w')

        self.lblApPat = tk.Label(self, text='Apellido Paterno: ')
        self.lblApPat.config(font=('Arial',10,'bold'), bg='#F5F5F5')
        self.lblApPat.grid(column=0, row=2, padx=10, pady=5, sticky='w')

        self.lblApMat = tk.Label(self, text='Apellido Materno: ')
        self.lblApMat.config(font=('Arial',10,'bold'), bg='#F5F5F5')
        self.lblApMat.grid(column=0, row=3, padx=10, pady=5, sticky='w')

        self.lblRut = tk.Label(self, text='RUT: ')
        self.lblRut.config(font=('Arial',10,'bold'), bg='#F5F5F5')
        self.lblRut.grid(column=0, row=4, padx=10, pady=5, sticky='w')

        self.lblFnac = tk.Label(self, text='Fecha de Nacimiento: ')
        self.lblFnac.config(font=('Arial',10,'bold'), bg='#F5F5F5')
        self.lblFnac.grid(column=0, row=5, padx=10, pady=5, sticky='w')

        self.lblEdad = tk.Label(self, text='Edad: ')
        self.lblEdad.config(font=('Arial',10,'bold'), bg='#F5F5F5')
        self.lblEdad.grid(column=0, row=6, padx=10, pady=5, sticky='w')

        self.lblCurso = tk.Label(self, text='Curso: ')
        self.lblCurso.config(font=('Arial',10,'bold'), bg='#F5F5F5')
        self.lblCurso.grid(column=0, row=7, padx=10, pady=5, sticky='w')

        self.lblAntecedentes = tk.Label(self, text='Antecedentes: ')
        self.lblAntecedentes.config(font=('Arial',10,'bold'), bg='#F5F5F5')
        self.lblAntecedentes.grid(column=0, row=8, padx=10, pady=5, sticky='w')

        self.lblCorreo = tk.Label(self, text='Correo: ')
        self.lblCorreo.config(font=('Arial',10,'bold'), bg='#F5F5F5')
        self.lblCorreo.grid(column=0, row=9, padx=10, pady=5, sticky='w')

        self.lblTelefono = tk.Label(self, text='Teléfono: ')
        self.lblTelefono.config(font=('Arial',10,'bold'), bg='#F5F5F5')
        self.lblTelefono.grid(column=0, row=10, padx=10, pady=5, sticky='w')

        #ENTRYS
        self.svNombre = tk.StringVar()
        self.entryNombre = tk.Entry(self, textvariable=self.svNombre)
        self.entryNombre.config(width=25, font=('Arial', 9))
        self.entryNombre.grid(column=1, row=1, padx=10, pady=5)

        self.svApPat = tk.StringVar()
        self.entryApPat = tk.Entry(self, textvariable=self.svApPat)
        self.entryApPat.config(width=25, font=('Arial', 9))
        self.entryApPat.grid(column=1, row=2, padx=10, pady=5)

        self.svApMat = tk.StringVar()
        self.entryApMat = tk.Entry(self, textvariable=self.svApMat)
        self.entryApMat.config(width=25, font=('Arial', 9))
        self.entryApMat.grid(column=1, row=3, padx=10, pady=5)

        self.svRut = tk.StringVar()
        self.entryRut = tk.Entry(self, textvariable=self.svRut)
        self.entryRut.config(width=25, font=('Arial', 9))
        self.entryRut.grid(column=1, row=4, padx=10, pady=5)
        
        self.svFnac = tk.StringVar()
        self.entryFnac = tk.Entry(self, textvariable=self.svFnac)
        self.entryFnac.config(width=25, font=('Arial', 9))
        self.entryFnac.grid(column=1, row=5, padx=10, pady=5)

        self.svEdad = tk.StringVar()
        self.entryEdad = tk.Entry(self, textvariable=self.svEdad)
        self.entryEdad.config(width=25, font=('Arial', 9))
        self.entryEdad.grid(column=1, row=6, padx=10, pady=5)

        self.svCurso = tk.StringVar()
        self.entryCurso = tk.Entry(self, textvariable=self.svCurso)
        self.entryCurso.config(width=25, font=('Arial', 9))
        self.entryCurso.grid(column=1, row=7, padx=10, pady=5)

        self.svAntecedentes = tk.StringVar()
        self.entryAntecedentes = tk.Entry(self, textvariable=self.svAntecedentes)
        self.entryAntecedentes.config(width=25, font=('Arial', 9))
        self.entryAntecedentes.grid(column=1, row=8, padx=10, pady=5)

        self.svCorreo = tk.StringVar()
        self.entryCorreo = tk.Entry(self, textvariable=self.svCorreo)
        self.entryCorreo.config(width=25, font=('Arial', 9))
        self.entryCorreo.grid(column=1, row=9, padx=10, pady=5)

        self.svTelefono = tk.StringVar()
        self.entryTelefono = tk.Entry(self, textvariable=self.svTelefono)
        self.entryTelefono.config(width=25, font=('Arial', 9))
        self.entryTelefono.grid(column=1, row=10, padx=10, pady=5)

        #BUTTONS

        self.btnNuevo = tk.Button(self, text='INGRESAR ESTUDIANTE', command=self.habilitar)
        self.btnNuevo.config(width=20, font=('Arial',11,'bold'), fg='#FFFFFF', 
                                            bg='#BD0000', cursor='hand2', activebackground='#FF0000', activeforeground='#FFFFFF')
        self.btnNuevo.grid(column=0,row=11, padx=10, pady=5)

        self.btnGuardar = tk.Button(self, text='GUARDAR', command=self.guardarPaciente)
        self.btnGuardar.config(width=20, font=('Arial',11,'bold'), fg='#FFFFFF', 
                                            bg='#BD0000', cursor='hand2', activebackground='#FF0000', activeforeground='#FFFFFF')
        self.btnGuardar.grid(column=1,row=11, padx=10, pady=5)

        self.btnCancelar = tk.Button(self, text='CANCELAR', command=self.deshabilitar)
        self.btnCancelar.config(width=20, font=('Arial',11,'bold'), fg='#FFFFFF', 
                                            bg='#BD0000', cursor='hand2', activebackground='#FF0000', activeforeground='#FFFFFF')
        self.btnCancelar.grid(column=2,row=11, padx=10, pady=5)

        #BUSCADOR
        #LABEL BUSCADOR
        self.lblBuscarRut = tk.Label(self, text='Buscar RUT: ')
        self.lblBuscarRut.config(font=('Arial',10,'bold'), bg='#F5F5F5')
        self.lblBuscarRut.grid(column=3, row=0, padx=10, pady=5, sticky='w')

        self.lblBuscarApellido = tk.Label(self, text='Buscar Apellido: ')
        self.lblBuscarApellido.config(font=('Arial',10,'bold'), bg='#F5F5F5')
        self.lblBuscarApellido.grid(column=3, row=1, padx=10, pady=5, sticky='w')

        #ENTRY BUSCADOR
        self.svBuscarRut = tk.StringVar()
        self.entryBuscarRut = tk.Entry(self, textvariable=self.svBuscarRut)
        self.entryBuscarRut.config(width=35, font=('Arial', 9))
        self.entryBuscarRut.grid(column=4, row=0, padx=10, pady=5, columnspan=2)

        self.svBuscarApellido = tk.StringVar()
        self.entryBuscarApellido = tk.Entry(self, textvariable=self.svBuscarApellido)
        self.entryBuscarApellido.config(width=35, font=('Arial', 9))
        self.entryBuscarApellido.grid(column=4, row=1, padx=10, pady=5, columnspan=2)

        #BOTON BUSCADOR
        self.btnBuscarCondicion = tk.Button(self, text='BUSCAR', command= self.buscarCondicion)
        self.btnBuscarCondicion.config(width=20, font=('Arial',11,'bold'), fg='#FFFFFF', 
                                            bg='#BD0000', cursor='hand2', activebackground='#FF0000', activeforeground='#FFFFFF')
        self.btnBuscarCondicion.grid(column=7,row=0, padx=10, pady=5)

        self.btnLimpiarBuscador = tk.Button(self, text='LIMPIAR', command= self.limpiarBuscador)
        self.btnLimpiarBuscador.config(width=20, font=('Arial',11,'bold'), fg='#FFFFFF', 
                                            bg='#BD0000', cursor='hand2', activebackground='#FF0000', activeforeground='#FFFFFF')
        self.btnLimpiarBuscador.grid(column=7,row=1, padx=10, pady=5)

       
        #BOTON CALENDARIO IMG
        self.calImg = tk.PhotoImage(file='img/calendar.png')
        self.btnCalendario = tk.Button(self, image=self.calImg, command= self.vistaCalendario)
        self.btnCalendario.config(width=20, height=20, font=('Arial',8,), fg='#FFFFFF', bg='#F5F5F5', cursor='hand2', activebackground='#F5F5F5', activeforeground='#F5F5F5')
        self.btnCalendario.grid(column=2,row=5, padx=10, pady=5, sticky='w')
        

    def vistaCalendario(self):
        self.calendario = Toplevel()
        self.calendario.title('F.de Nac.')
        self.calendario.resizable(0,0)
        self.calendario.iconbitmap('img/logo-circular.ico')
        self.calendario.config(bg='#F5F5F5')

        self.svCalendario = StringVar()
        self.cal = tc.Calendar(self.calendario, selectmode='day', year=2000, month=1, day=1, locale='es_US',  bg='#777777', fg='#FFFFFF', headersbackground='#B6DDFE', cursor =' hand2', date_pattern='dd-mm-Y')
        self.cal.pack(pady=22)
        self.cal.grid(row=1, column = 0)
        self.btnSeleccionar = tk.Button(self.calendario, text='SELECCIONAR', command= self.establecer)
        self.btnSeleccionar.config(width=10, font=('Arial',6,'bold'), fg='#FFFFFF', 
                                            bg='#BD0000', cursor='hand2', activebackground='#FF0000', activeforeground='#FFFFFF')
        self.btnSeleccionar.grid(column=0,row=2, padx=10, pady=5)
        #LBL 
        self.lbldate = tk.Label(self, text='')
        self.lbldate.grid(column=1, row=0, padx=10, pady=5, sticky='w')

        self.svCalendario.trace('w', self.establecer)

          
    def establecer(self, *args):        
        self.svFnac.set(self.cal.get_date())
        if len(self.cal.get_date()) > 1:
        
            self.fechaActual = date.today()
            self.date1 = self.cal.get_date()
            self.conver = datetime.strptime(self.date1, "%d-%m-%Y")

            self.resul = self.fechaActual.year - self.conver.year
            self.resul -= ((self.fechaActual.month, self.fechaActual.day) < (self.conver.month, self.conver.day))
            self.svEdad.set(self.resul)
            self.calendario.destroy()
     
    
    def limpiarBuscador(self):
        self.svBuscarApellido.set('')
        self.svBuscarRut.set('')
        self.tablaPaciente()



    def buscarCondicion(self):
        if len(self.svBuscarRut.get()) > 0 or len(self.svBuscarApellido.get()) > 0:
            where = "WHERE 1=1"
            if (len(self.svBuscarRut.get())) > 0:
                where = "WHERE rut = " + self.svBuscarRut.get() + "" #WHERE rut = 87878787
            if (len(self.svBuscarApellido.get())) > 0:
                ehere = "WHERE apellidoPaterno LIKE '" + self.svBuscarApellido.get()+"%' AND activo = 1"
            
            self.tablaPaciente(where)
        else:
            self.tablaPaciente()



    def guardarPaciente(self):
        persona = Persona(
        self.svNombre.get(), self.svApPat.get(), self.svApMat.get(), self.svRut.get(), self.svFnac.get(), self.svEdad.get(), self.svCurso.get(), self.svAntecedentes.get(), self.svCorreo.get(), self.svTelefono.get()
        )

        if self.idPersona == None:
            guardarDatoPaciente(persona)
        else:
            editarDatoPaciente(persona, self.idPersona)

       
        self.deshabilitar()
        self.tablaPaciente()

    def habilitar(self):
        self.svNombre.set('')
        self.svApPat.set('')
        self.svApMat.set('')
        self.svRut.set('')
        self.svFnac.set('')
        self.svEdad.set('')
        self.svCurso.set('')
        self.svAntecedentes.set('')
        self.svCorreo.set('')
        self.svTelefono.set('') 

        self.entryNombre.config(state='normal')
        self.entryApPat.config(state='normal')
        self.entryApMat.config(state='normal')
        self.entryRut.config(state='normal')
        self.entryFnac.config(state='normal')
        self.entryEdad.config(state='normal')
        self.entryCurso.config(state='normal')
        self.entryAntecedentes.config(state='normal')
        self.entryCorreo.config(state='normal')
        self.entryTelefono.config(state='normal')

        self.btnGuardar.config(state='normal')
        self.btnCancelar.config(state='normal')
        self.btnCalendario.config(state='normal')

    def deshabilitar(self):
        
        self.idPersona = None
        self.svNombre.set('')
        self.svApPat.set('')
        self.svApMat.set('')
        self.svRut.set('')
        self.svFnac.set('')
        self.svEdad.set('')
        self.svCurso.set('')
        self.svAntecedentes.set('')
        self.svCorreo.set('')
        self.svTelefono.set('') 

        self.entryNombre.config(state='disable')
        self.entryApPat.config(state='disable')
        self.entryApMat.config(state='disable')
        self.entryRut.config(state='disable')
        self.entryFnac.config(state='disable')
        self.entryEdad.config(state='disable')
        self.entryCurso.config(state='disable')
        self.entryAntecedentes.config(state='disable')
        self.entryCorreo.config(state='disable')
        self.entryTelefono.config(state='disable')
        self.btnCalendario.config(state='disable')

        self.btnGuardar.config(state='disabled')
        self.btnCancelar.config(state='disabled')

    def tablaPaciente(self, where=""):

        if len(where) > 0:
            self.listaPersona = listarCondicion(where)
        else:
            self.listaPersona = listar()
            #self.listaPersona.reverse()

        self.tabla = ttk.Treeview(self, column=('Nombre','ApPat','ApMat','Rut','Fnac','Edad','Curso','Antecedentes','Correo','Teléfono'))
        self.tabla.grid(column=0, row=12, columnspan=11, sticky='nse')

        self.scroll = ttk.Scrollbar(self, orient='vertical', command=self.tabla.yview)
        self.scroll.grid(row=12, column=12, sticky='nse')

        self.tabla.configure(yscrollcommand=self.scroll.set)

        self.tabla.tag_configure('evenrow', background='#D5F0FB')

        self.tabla.heading('#0', text='ID')
        self.tabla.heading('#1', text='Nombre')
        self.tabla.heading('#2', text='Ap. Paterno')
        self.tabla.heading('#3', text='Ap. Materno')
        self.tabla.heading('#4', text='RUT')
        self.tabla.heading('#5', text='Fecha de Nac.')
        self.tabla.heading('#6', text='Edad')
        self.tabla.heading('#7', text='Curso')
        self.tabla.heading('#8', text='Antecedentes')
        self.tabla.heading('#9', text='Correo')
        self.tabla.heading('#10', text='Teléfono')

        self.tabla.column('#0', anchor=W, width=50)
        self.tabla.column('#1', anchor=W, width=150)
        self.tabla.column('#2', anchor=W, width=120)
        self.tabla.column('#3', anchor=W, width=120)
        self.tabla.column('#4', anchor=W, width=80)
        self.tabla.column('#5', anchor=W, width=100)
        self.tabla.column('#6', anchor=W, width=50)
        self.tabla.column('#7', anchor=W, width=50)
        self.tabla.column('#8', anchor=W, width=300)
        self.tabla.column('#9', anchor=W, width=250)
        self.tabla.column('#10', anchor=W, width=85)

        for p in self.listaPersona:

            self.tabla.insert('',0,text=p[0], values=(p[1],p[2],p[3],p[4],p[5],p[6],p[7],p[8],p[9],p[10]), tags=('evenrow',))

        self.btnEditarPaciente = tk.Button(self, text='EDITAR ESTUDIANTE', command=self.editarPaciente)
        self.btnEditarPaciente.config(width=20,font=('ARIAL',10,'bold'), fg='#FFFFFF', bg='#BD0000', activebackground='#FF0000', activeforeground='#FFFFFF', cursor='hand2')
        self.btnEditarPaciente.grid(row=13, column=0, padx=10, pady=5)

        self.btnEliminarPaciente = tk.Button(self, text='ELIMINAR ESTUDIANTE', command= self.eliminarDatoPaciente)
        self.btnEliminarPaciente.config(width=20,font=('ARIAL',10,'bold'), fg='#FFFFFF', bg='#BD0000', activebackground='#FF0000', activeforeground='#FFFFFF', cursor='hand2')
        self.btnEliminarPaciente.grid(row=13, column=1, padx=10, pady=5)

        self.btnHistorialPaciente = tk.Button(self, text='HISTORIAL ESTUDIANTE', command=self.historiaMedica)
        self.btnHistorialPaciente.config(width=20,font=('ARIAL',10,'bold'), fg='#FFFFFF', bg='#BD0000', activebackground='#FF0000', activeforeground='#FFFFFF', cursor='hand2')
        self.btnHistorialPaciente.grid(row=13, column=2, padx=10, pady=5)

        self.btnSalir = tk.Button(self, text='SALIR', command=self.root.destroy)
        self.btnSalir.config(width=20,font=('ARIAL',10,'bold'), fg='#FFFFFF', bg='#000000', activebackground='#FF0000', activeforeground='#FFFFFF', cursor='hand2')
        self.btnSalir.grid(row=13, column=6, padx=10, pady=5)
       
        self.btnAd = tk.Button(self, text='Acerca de', command=self.topAcercaDe)
        self.btnAd.config(width=20,font=('ARIAL',10,'bold'), fg='#FFFFFF', bg='#000000', activebackground='#FF0000', activeforeground='#FFFFFF', cursor='hand2')
        self.btnAd.grid(row=13, column=7, padx=10, pady=5)

    def topAcercaDe(self):
        self.topAD = Toplevel()
        self.topAD.title('Acerca de')
        self.topAD.resizable(0,0)
        self.topAD.iconbitmap('img/logo-circular.ico')
        self.topAD.config(bg='#F5F5F5')

        self.frameLogo = tk.LabelFrame(self.topAD)
        self.frameLogo.config(bg='#F5F5F5')
        self.frameLogo.pack(fill="both", expand="yes", pady=10, padx=20)

        self.frameTxt = tk.LabelFrame(self.topAD)
        self.frameTxt.config(bg='#F5F5F5')
        self.frameTxt.pack(fill="both", expand="yes", pady=10, padx=20)

        self.logo = tk.PhotoImage(file='img/Logo-Circular.png')
        self.lblAcercade0 = tk.Label(self.frameLogo, image=self.logo, width=200, height=200, bg='#F5F5F5').pack()
        self.lblAcercade1 = tk.Label(self.frameTxt, text='REGISTROS MÉDICOS BETTERLAND', width=100, font=('ARIAL', 10, 'bold'), bg='#F5F5F5')
        self.lblAcercade1.grid(row=1, column=0, padx=0, pady=3, sticky='w')
        self.lblAcercade2 = tk.Label(self.frameTxt, text='Version 1.0', width=100, font=('ARIAL', 10, 'bold'), bg='#F5F5F5')
        self.lblAcercade2.grid(row=2, column=0, padx=0, pady=3, sticky='w')
        self.lblAcercade3 = tk.Label(self.frameTxt, text='Diseñado por Oliver Arias, Santiago, Noviembre de 2022', width=100, font=('ARIAL', 10), bg='#F5F5F5')
        self.lblAcercade3.grid(row=3, column=0, padx=0, pady=3, sticky='w')



    def historiaMedica(self):

        try:
            if self.idPersona == None:
                self.idPersona = self.tabla.item(self.tabla.selection())['text']
                self.idPersonaHistoria = self.tabla.item(self.tabla.selection())['text']
            if(self.idPersona > 0):
                idPersona = self.idPersona

            self.topHistoriaMedica = Toplevel()
            self.topHistoriaMedica.title('HISTORIAL ESTUDIANTE')
            self.topHistoriaMedica.resizable(0,0)
            self.topHistoriaMedica.iconbitmap('img/logo-circular.ico')
            self.topHistoriaMedica.config(bg='#F5F5F5')

            self.listaHistoria = listarHistoria(idPersona)
            self.tablaHistoria = ttk.Treeview(self.topHistoriaMedica, column=('Apellidos','Fecha Historia','Motivo','Examen Auxiliar','Tratamiento','Detalle'))
            self.tablaHistoria.grid(row=0, column=0, columnspan=7, sticky='nse')

            self.scrollHistoria = ttk.Scrollbar(self.topHistoriaMedica, orient='vertical', command=self.tablaHistoria.yview)
            self.scrollHistoria.grid(row=0, column=8, sticky='nse')
            self.tablaHistoria.configure(yscrollcommand=self.scrollHistoria.set)

            self.tablaHistoria.heading('#0', text='ID')
            self.tablaHistoria.heading('#1', text='Apellidos')
            self.tablaHistoria.heading('#2', text='Fecha y Hora')
            self.tablaHistoria.heading('#3', text='Motivo')
            self.tablaHistoria.heading('#4', text='Examen Auxiliar')
            self.tablaHistoria.heading('#5', text='Tratamiento')
            self.tablaHistoria.heading('#6', text='Detalle')

            self.tablaHistoria.column('#0', anchor=W, width=50)
            self.tablaHistoria.column('#1', anchor=W, width=100)
            self.tablaHistoria.column('#2', anchor=W, width=100)
            self.tablaHistoria.column('#3', anchor=W, width=120)
            self.tablaHistoria.column('#4', anchor=W, width=250)
            self.tablaHistoria.column('#5', anchor=W, width=200)
            self.tablaHistoria.column('#6', anchor=W, width=500)

            for p in self.listaHistoria:
                self.tablaHistoria.insert('',0, text=p[0], values=(p[1],p[2],p[3],p[4],p[5],p[6]))
            
            self.btnGuardarHistoria = tk.Button(self.topHistoriaMedica, text='Agregar Historia', command=self.topAgregarHistoria)
            self.btnGuardarHistoria.config(width=20,font=('ARIAL',10,'bold'), fg='#FFFFFF', bg='#BD0000', activebackground='#FF0000', activeforeground='#FFFFFF', cursor='hand2')
            self.btnGuardarHistoria.grid(row=2, column=0, padx=10, pady=5)

            self.btneditarHistoria = tk.Button(self.topHistoriaMedica, text='Editar Historia', command=self.topEditarHistorialMedico)
            self.btneditarHistoria.config(width=20,font=('ARIAL',10,'bold'), fg='#FFFFFF', bg='#BD0000', activebackground='#FF0000', activeforeground='#FFFFFF', cursor='hand2')
            self.btneditarHistoria.grid(row=2, column=1, padx=10, pady=5)

            self.btneliminarHistoria = tk.Button(self.topHistoriaMedica, text='Eliminar Historia', command=self.eliminarHistorialMedico)
            self.btneliminarHistoria.config(width=20,font=('ARIAL',10,'bold'), fg='#FFFFFF', bg='#BD0000', activebackground='#FF0000', activeforeground='#FFFFFF', cursor='hand2')
            self.btneliminarHistoria.grid(row=2, column=2, padx=10, pady=5)

            self.btnsalirHistoria = tk.Button(self.topHistoriaMedica, text='Salir', command=self.salirTop)
            self.btnsalirHistoria.config(width=20,font=('ARIAL',10,'bold'), fg='#FFFFFF', bg='#000000', activebackground='#FF0000', activeforeground='#FFFFFF', cursor='hand2')
            self.btnsalirHistoria.grid(row=2, column=6, padx=10, pady=5)
        
        except:
            title= 'Historia Médica'
            mensaje = 'Error al mostrar historial'
            messagebox.showerror(title, mensaje)

    def topAgregarHistoria(self):
        self.topAHistoria = Toplevel()
        self.topAHistoria.title('AGREGAR HISTORIA')
        self.topAHistoria.resizable(0,0)
        self.topAHistoria.iconbitmap('img/logo-circular.ico')
        self.topAHistoria.config(bg='#F5F5F5')

        #FRAME 1

        self.frameDatosHistoria = tk.LabelFrame(self.topAHistoria)
        self.frameDatosHistoria.config(bg='#F5F5F5')
        self.frameDatosHistoria.pack(fill="both", expand="yes", pady=10, padx=20)

        #LABELS AGREGAR HISTORIA MEDICA

        self.lblMotivoHistoria = tk.Label(self.frameDatosHistoria, text='Motivo', width=20, font=('ARIAL', 10, 'bold'), bg='#F5F5F5')
        self.lblMotivoHistoria.grid(row=1, column=0, padx=0, pady=3, sticky='w')

        self.lblExamenAuxiliarHistoria = tk.Label(self.frameDatosHistoria, text='Examen Auxiliar', width=20, font=('ARIAL', 10, 'bold'), bg='#F5F5F5')
        self.lblExamenAuxiliarHistoria.grid(row=3, column=0, padx=5, pady=3, sticky='w')

        self.lblTratamientoHistoria = tk.Label(self.frameDatosHistoria, text='Tratamiento', width=20, font=('ARIAL', 10, 'bold'), bg='#F5F5F5')
        self.lblTratamientoHistoria.grid(row=5, column=0, padx=5, pady=3, sticky='w')

        self.lblDetalleHistoria = tk.Label(self.frameDatosHistoria, text='Detalle', width=20, font=('ARIAL', 10, 'bold'), bg='#F5F5F5')
        self.lblDetalleHistoria.grid(row=7, column=0, padx=5, pady=3, sticky='w')

        #ENTRYS HISTORIA MEDICA

        self.svMotivoHistoria = tk.StringVar()
        self.motivoHistoria = tk.Entry(self.frameDatosHistoria, textvariable=self.svMotivoHistoria)
        self.motivoHistoria.config(width=70, font=('ARIAL', 10))
        self.motivoHistoria.grid(row=2, column=0, padx=5, pady=3, columnspan=2)

        self.svExamenAuxiliarHistoria = tk.StringVar()
        self.examenAuxiliarHistoria = tk.Entry(self.frameDatosHistoria, textvariable=self.svExamenAuxiliarHistoria)
        self.examenAuxiliarHistoria.config(width=70, font=('ARIAL', 10))
        self.examenAuxiliarHistoria.grid(row=4, column=0, padx=5, pady=3, columnspan=2)

        self.svTratamientoHistoria = tk.StringVar()
        self.tratamientoHistoria = tk.Entry(self.frameDatosHistoria, textvariable=self.svTratamientoHistoria)
        self.tratamientoHistoria.config(width=70, font=('ARIAL', 10))
        self.tratamientoHistoria.grid(row=6, column=0, padx=5, pady=3, columnspan=2)

        self.svDetalleHistoria = tk.StringVar()
        self.detalleHistoria = tk.Entry(self.frameDatosHistoria, textvariable=self.svDetalleHistoria)
        self.detalleHistoria.config(width=70, font=('ARIAL', 10))
        self.detalleHistoria.grid(row=8, column=0, padx=5, pady=3, rowspan=3)

        #FRAME 2
        self.frameFechaHistoria = tk.LabelFrame(self.topAHistoria)
        self.frameFechaHistoria.config(bg='#F5F5F5')
        self.frameFechaHistoria.pack(fill="both", expand="yes", padx=20, pady=10)

        #LABEL FECHA AGREGAR HISTORIA
        self.labelFechaHistoria = tk.Label(self.frameFechaHistoria, text='Fecha y Hora', width=20, font=('ARIAL', 10), bg='#F5F5F5')
        self.labelFechaHistoria.grid(row=1, column=0, padx=5, pady=3, sticky='w')

        #ENTRY FECHA HISTORIA
        self.svFechaHistoria = tk.StringVar()
        self.entryFechaHistoria = tk.Entry(self.frameFechaHistoria, textvariable=self.svFechaHistoria)
        self.entryFechaHistoria.config(width=20, font=('ARIAL', 10,))
        self.entryFechaHistoria.grid(row=1, column=1, padx=5, pady=3)
        #TRAER FECHA Y HORA ACTUAL
        self.svFechaHistoria.set(datetime.today().strftime('%d-%m-%Y %H:%M'))

        #BUTTONS AGREGAR HISTORIA
        self.btnAgregarHistoria = tk.Button(self.frameFechaHistoria, text='AGREGAR', command=self.agregarHistorialMedico)
        self.btnAgregarHistoria.config(width=20,font=('ARIAL',10,'bold'), fg='#FFFFFF', bg='#BD0000', activebackground='#FF0000', activeforeground='#FFFFFF', cursor='hand2')
        self.btnAgregarHistoria.grid(row=2, column=0, padx=10, pady=5)

        self.btnSalirAgregarHistoria = tk.Button(self.frameFechaHistoria, text='SALIR', command=self.topAHistoria.destroy)
        self.btnSalirAgregarHistoria.config(width=20,font=('ARIAL',10,'bold'), fg='#FFFFFF', bg='#000000', activebackground='#FF0000', activeforeground='#FFFFFF', cursor='hand2')
        self.btnSalirAgregarHistoria.grid(row=2, column=3, padx=10, pady=5)

           
    def agregarHistorialMedico(self):
        try:
            if self.idHistoriaMedica == None:
                guardarHistoria(self.idPersonaHistoria, self.svFechaHistoria.get(), self.svMotivoHistoria.get(), self.svExamenAuxiliarHistoria.get(), self.svTratamientoHistoria.get(), self.svDetalleHistoria.get())
            self.topAHistoria.destroy()
            self.topHistoriaMedica.destroy()
        except:
            title='Agregar Historia'
            mensaje='Error al Agregar historia Médica'
            messagebox.showerror(title, mensaje)

    def eliminarHistorialMedico(self):
        try:
            self.idHistoriaMedica = self.tablaHistoria.item(self.tablaHistoria.selection())['text']
            eliminarHistoria(self.idHistoriaMedica)

            self.historiaMedica = None
            self.topHistoriaMedica.destroy()

        except:
            title='Eliminar Historia'
            mensaje='Error al eliminar'
            messagebox.showerror(title, mensaje)


    def topEditarHistorialMedico(self):
        try:
            self.idHistoriaMedica = self.tablaHistoria.item(self.tablaHistoria.selection())['text']
            self.fechaHistoriaEditar = self.tablaHistoria.item(self.tablaHistoria.selection())['values'][1]
            self.motivoHistoriaEditar = self.tablaHistoria.item(self.tablaHistoria.selection())['values'][2]
            self.examenAuxiliarHistoriaEditar = self.tablaHistoria.item(self.tablaHistoria.selection())['values'][3]
            self.tratamientoHistoriaEditar = self.tablaHistoria.item(self.tablaHistoria.selection())['values'][4]
            self.detalleHistoriaEditar = self.tablaHistoria.item(self.tablaHistoria.selection())['values'][5]

            self.topEditarHistoria = Toplevel()
            self.topEditarHistoria.title('EDITAR HISTORIA MEDICA')
            self.topEditarHistoria.resizable(0,0)
            self.topEditarHistoria.iconbitmap('img/logo-circular.ico')
            self.topEditarHistoria.config(bg='#F5F5F5')

            #FRAME EDITAR DATOS HISTORIA
            self.frameEditarHistoria = tk.LabelFrame(self.topEditarHistoria)
            self.frameEditarHistoria.config(bg='#F5F5F5')
            self.frameEditarHistoria.pack(fill="both", expand="yes", padx=20, pady=10)

            #LABELS EDITAR HISTORIA
            self.lblMotivoEditar = tk.Label(self.frameEditarHistoria, text='Motivo de la historia', width=30, font=('ARIAL', 10, 'bold'), bg='#F5F5F5')
            self.lblMotivoEditar.grid(row=1, column=0, padx=5, pady=3)

            self.lblExamenAuxiliarEditar = tk.Label(self.frameEditarHistoria, text='Exámen Auxiliar', width=30, font=('ARIAL', 10, 'bold'), bg='#F5F5F5')
            self.lblExamenAuxiliarEditar.grid(row=3, column=0, padx=5, pady=3)

            self.lblTratamientoEditar = tk.Label(self.frameEditarHistoria, text='Tratamiento', width=30, font=('ARIAL', 10, 'bold'), bg='#F5F5F5')
            self.lblTratamientoEditar.grid(row=5, column=0, padx=5, pady=3)

            self.lblDetalleEditar = tk.Label(self.frameEditarHistoria, text='Detalle', width=30, font=('ARIAL', 10, 'bold'), bg='#F5F5F5')
            self.lblDetalleEditar.grid(row=7, column=0, padx=5, pady=3)

            #ENTRYS EDITAR HISTORIA

            self.svMotivoEditar = tk.StringVar()
            self.entryMotivoEditar = tk.Entry(self.frameEditarHistoria, textvariable=self.svMotivoEditar)
            self.entryMotivoEditar.config(width=65, font=('ARIAL', 10))
            self.entryMotivoEditar.grid(row=2, column=0, pady=3, padx=5, columnspan=2)

            self.svExamenAuxiliarEditar = tk.StringVar()
            self.entryExamenAuxiliarEditar = tk.Entry(self.frameEditarHistoria, textvariable=self.svExamenAuxiliarEditar)
            self.entryExamenAuxiliarEditar.config(width=65, font=('ARIAL', 10))
            self.entryExamenAuxiliarEditar.grid(row=4, column=0, pady=3, padx=5, columnspan=2)

            self.svTratamientoEditar = tk.StringVar()
            self.entryTratamientoEditar = tk.Entry(self.frameEditarHistoria, textvariable=self.svTratamientoEditar)
            self.entryTratamientoEditar.config(width=65, font=('ARIAL', 10))
            self.entryTratamientoEditar.grid(row=6, column=0, pady=3, padx=5, columnspan=2)

            self.svDetalleEditar = tk.StringVar()
            self.entryDetalleEditar = tk.Entry(self.frameEditarHistoria, textvariable=self.svDetalleEditar)
            self.entryDetalleEditar.config(width=65, font=('ARIAL', 10))
            self.entryDetalleEditar.grid(row=8, column=0, pady=3, padx=5, columnspan=2)

            #FRAME FECHA EDITAR
            self.frameFechaEditar = tk.LabelFrame(self.topEditarHistoria)
            self.frameFechaEditar.config(bg='#F5F5F5')
            self.frameFechaEditar.pack(fill="both", expand="yes", padx=20, pady=10)
            #LABEL FECHA EDITAR
            self.lblFechaHistoriaEditar = tk.Label(self.frameFechaEditar, text='Fecha y Hora', width=30, font=('ARIAL', 10, 'bold'), bg='#F5F5F5')
            self.lblFechaHistoriaEditar.grid(row=1, column=0, padx=5, pady=3)

            #ENTRY FECH EDITAR
            self.svFechaHistoriaEditar = tk.StringVar()
            self.entryFechaHistoriaEditar = tk.Entry(self.frameFechaEditar, textvariable=self.svFechaHistoriaEditar)
            self.entryFechaHistoriaEditar.config(width=65, font=('ARIAL', 10))
            self.entryFechaHistoriaEditar.grid(row=1, column=1, pady=3, padx=5)

            #INSERTAR LOS VALORES A LOS ENTRYS
            self.entryMotivoEditar.insert(0, self.motivoHistoriaEditar)
            self.entryExamenAuxiliarEditar.insert(0, self.examenAuxiliarHistoriaEditar)
            self.entryTratamientoEditar.insert(0, self.tratamientoHistoriaEditar)
            self.entryDetalleEditar.insert(0, self.detalleHistoriaEditar)
            self.entryFechaHistoriaEditar.insert(0, self.fechaHistoriaEditar)

            #BUTTON EDITAR HISTORIA
            self.btneditarHistoriaMedica = tk.Button(self.frameFechaEditar, text='Editar Historia', command=self.historiaMedicaEditar)
            self.btneditarHistoriaMedica.config(width=20,font=('ARIAL',10,'bold'), fg='#FFFFFF', bg='#BD0000', activebackground='#FF0000', activeforeground='#FFFFFF', cursor='hand2')
            self.btneditarHistoriaMedica.grid(row=2, column=0, padx=10, pady=5)

            self.btnsalirEditarHistoriaMedica = tk.Button(self.frameFechaEditar, text='Salir', command=self.topEditarHistoria.destroy)
            self.btnsalirEditarHistoriaMedica.config(width=20,font=('ARIAL',10,'bold'), fg='#FFFFFF', bg='#000000', activebackground='#FF0000', activeforeground='#FFFFFF', cursor='hand2')
            self.btnsalirEditarHistoriaMedica.grid(row=2, column=3, padx=10, pady=5)

            if self.idHistoriaMedicaEditar == None:
                self.idHistoriaMedicaEditar = self.idHistoriaMedica
            self.idHistoriaMedica = None
        except:
            title ='Editar Historia'
            mensaje='Error al editar Historia'
            messagebox.showerror(title, mensaje)
             
    def historiaMedicaEditar(self):
        try:
            editarHistoria(self.svFechaHistoriaEditar.get(), self.svMotivoEditar.get(), self.svExamenAuxiliarEditar.get(),self.svTratamientoEditar.get(), self.svDetalleEditar.get(), self.idHistoriaMedicaEditar)
            self.idHistoriaMedicaEditar = None
            self.idHistoriaMedica = None
            self.topEditarHistoria.destroy()
            self.topHistoriaMedica.destroy()

        except:
            title = 'Editar Historia'
            mensaje = 'Error al editar historia'
            messagebox.showerror(title, mensaje)
            self.topEditarHistoria.destroy()


    def salirTop(self):
        self.topHistoriaMedica.destroy()

      
        

    def editarPaciente(self):

        try:
            self.idPersona = self.tabla.item(self.tabla.selection())['text'] #Trae el IdPaciente
            self.nombrePaciente = self.tabla.item(self.tabla.selection())['values'][0]
            self.apellidoPaternoPaciente = self.tabla.item(self.tabla.selection())['values'][1]
            self.apellidoMaternoPaciente = self.tabla.item(self.tabla.selection())['values'][2]
            self.rutPaciente = self.tabla.item(self.tabla.selection())['values'][3]
            self.FnacPaciente = self.tabla.item(self.tabla.selection())['values'][4]
            self.edadPaciente = self.tabla.item(self.tabla.selection())['values'][5]
            self.cursoPaciente = self.tabla.item(self.tabla.selection())['values'][6]
            self.antecedentesPaciente = self.tabla.item(self.tabla.selection())['values'][7]
            self.correoPaciente= self.tabla.item(self.tabla.selection())['values'][8]
            self.telefonoPaciente = self.tabla.item(self.tabla.selection())['values'][9]

            self.habilitar()

            self.entryNombre.insert(0, self.nombrePaciente)
            self.entryApPat.insert(0, self.apellidoPaternoPaciente)
            self.entryApMat.insert(0, self.apellidoMaternoPaciente)
            self.entryRut.insert(0, self.rutPaciente)
            self.entryFnac.insert(0, self.FnacPaciente)
            self.entryEdad.insert(0, self.edadPaciente)
            self.entryCurso.insert(0, self.cursoPaciente)
            self.entryAntecedentes.insert(0, self.antecedentesPaciente)
            self.entryCorreo.insert(0, self.correoPaciente)
            self.entryTelefono.insert(0, self.telefonoPaciente)

        except:
            title = 'EDITAR ESTUDIANTE'
            mensaje = 'ERROR AL EDITAR ESTUDIANTE'
            messagebox.showerror(title, mensaje)

    def eliminarDatoPaciente(self):
        try:
            self.idPersona = self.tabla.item(self.tabla.selection())['text']
            eliminarPaciente(self.idPersona)
          
            self.tablaPaciente()
            self.idPersona = None
        except:
            title = 'ELIMINAR ESTUDIANTE'
            mensaje = 'ERROR AL ELIMINAR ESTUDIANTE'
            messagebox.showerror(title, mensaje)