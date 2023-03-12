# coding: utf-8
from sqlalchemy import Boolean, Column, Date, Float, ForeignKey, Integer, String, Table, text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

from config.db import engine

Base = declarative_base()
metadata = Base.metadata


class Departamentos(Base):
    __tablename__ = 'departamentos'

    id_departamento = Column(Integer, primary_key=True,autoincrement=True)
    nombre_departamento = Column(String, nullable=False)

    facultad = relationship('Facultad', secondary='facultad_departamentos')


class Facultad(Base):
    __tablename__ = 'facultad'

    id_facultad = Column(Integer, primary_key=True, autoincrement=True)
    nombre_facultad = Column(String, nullable=False)


class ProgramasAcademicos(Base):
    __tablename__ = 'programas_academicos'

    codigo_programa = Column(Integer, primary_key=True, autoincrement=False)
    nombre_programa = Column(String, nullable=False)

    departamentos = relationship('Departamentos', secondary='departamento_programas')



t_departamento_programas = Table(
    'departamento_programas', metadata,
    Column('codigo_programa', ForeignKey('programas_academicos.codigo_programa'), nullable=False),
    Column('id_departamento', ForeignKey('departamentos.id_departamento'), nullable=False)
)


t_facultad_departamentos = Table(
    'facultad_departamentos', metadata,
    Column('id_facultad', ForeignKey('facultad.id_facultad'), nullable=False),
    Column('id_departamento', ForeignKey('departamentos.id_departamento'), nullable=False)
)

metadata.create_all(engine)