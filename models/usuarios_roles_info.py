# coding: utf-8
from sqlalchemy import Boolean, Column, Date, Float, ForeignKey, Integer, String, Table, text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

from config.db import engine

from models.programas_facultades_departamentos import ProgramasAcademicos

Base = declarative_base()
metadata = Base.metadata

class Rol(Base):
    __tablename__ = 'rol'

    rol = Column(String, nullable=False)
    rol_id = Column(Integer, primary_key=True,autoincrement=True)

    usuarios = relationship('Usuarios', secondary='usuario_rol')

class Usuarios(Base):
    __tablename__ = 'usuarios'

    usuario_un = Column(String, primary_key=True)
    estado = Column(Boolean, nullable=False)
    nombres = Column(String, nullable=False)
    apellidos = Column(String, nullable=False)
    documento = Column(String, nullable=False)
    tipo_documento = Column(Boolean, nullable=False)

class InformacionPersonal(Usuarios):
    __tablename__ = 'informacion_personal'

    fecha_nacimiento = Column(Date, nullable=False)
    sexo = Column(Boolean, nullable=False)
    ciudad_nacimiento = Column(String, nullable=False)
    direccion_residencia = Column(String, nullable=False)
    ciudad_residencia = Column(String, nullable=False)
    telefono = Column(String, nullable=False)
    correo_alterno = Column(String, nullable=False)
    eps = Column(String, nullable=False)
    hijos = Column(Boolean, nullable=False)
    nombre_apellido_acudiente = Column(String, nullable=False)
    relacion_acudiente = Column(String, nullable=False)
    telefono_acudiente = Column(String, nullable=False)
    usuario_un = Column(ForeignKey('usuarios.usuario_un'), primary_key=True)

class InformacionAcademica(Base):
    __tablename__ = 'informacion_academica'

    historia_academica = Column(Integer, primary_key=True, autoincrement=False)
    porcentaje_de_avance = Column(Float, nullable=False)
    estado_historia = Column(Boolean, nullable=False)
    papi = Column(Float, nullable=False)
    papa = Column(Float, nullable=False)
    codigo_programa_academico = Column(Integer, ForeignKey(ProgramasAcademicos.codigo_programa), nullable=False)

    #programas_academicos = relationship('ProgramasAcademicos')
    usuarios = relationship('Usuarios', secondary='historia_academica_estudiantes')


t_usuario_rol = Table(
    'usuario_rol', metadata,
    Column('rol_id', ForeignKey('rol.rol_id'), primary_key=True, nullable=False),
    Column('usuario_un', ForeignKey('usuarios.usuario_un'), primary_key=True, nullable=False)
)


t_historia_academica_estudiantes = Table(
    'historia_academica_estudiantes', metadata,
    Column('cod_historia_acdemica', ForeignKey('informacion_academica.historia_academica'), primary_key=True, nullable=False),
    Column('usuario_un', ForeignKey('usuarios.usuario_un'), primary_key=True, nullable=False)
)


metadata.create_all(engine)