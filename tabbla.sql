CREATE TABLE Agente
(
  Codigo_Agente  NOT NULL,
  Nombre        ,
  Direccion     ,
  DNI           ,
  Codigo_Broker  NOT NULL,
  CONSTRAINT PK_Agente PRIMARY KEY (Codigo_Agente)
)
GO

EXECUTE sys.sp_addextendedproperty 'MS_Description',
  'Broker', 'user', dbo, 'table', 'Agente'
GO

CREATE TABLE Asegurados
(
  Nombre           ,
  DNI_Asegurado     NOT NULL,
  Sueldo           ,
  Telefono         ,
  Fecha_Nacimiento ,
  Direccion        ,
  CONSTRAINT PK_Asegurados PRIMARY KEY (DNI_Asegurado)
)
GO

CREATE TABLE Beneficiario
(
  Dni_beneficiario        NOT NULL,
  Nombre                 ,
  Sueldo                 ,
  Telefono               ,
  Fecha_Nacimiento       ,
  Direccion_Beneficiario ,
  CONSTRAINT PK_Beneficiario PRIMARY KEY (Dni_beneficiario)
)
GO

CREATE TABLE Broker
(
  Codigo_Broker  NOT NULL,
  RUC           ,
  Razón Social  ,
  CONSTRAINT PK_Broker PRIMARY KEY (Codigo_Broker)
)
GO

CREATE TABLE Pago
(
  PagoID  NOT NULL,
  Tipo   ,
  CONSTRAINT PK_Pago PRIMARY KEY (PagoID)
)
GO

CREATE TABLE Poliza
(
  Id_poliza              NOT NULL,
  Fecha_Contratacion    ,
  Fecha_Vigencia        ,
  Tipo_Producto         ,
  Suma_Asegurada        ,
  Contratante           ,
  Direccion_Facturacion ,
  Cobertura_poliza      ,
  DNI_Asegurado          NOT NULL,
  Dni_beneficiario       NOT NULL,
  Codigo_Agente          NOT NULL,
  PagoID                 NOT NULL,
  CONSTRAINT PK_Poliza PRIMARY KEY (Id_poliza)
)
GO

EXECUTE sys.sp_addextendedproperty 'MS_Description',
  'Persona natural o juridica', 'user', dbo, 'table', 'Poliza', 'column', 'Contratante'
GO

ALTER TABLE Poliza
  ADD CONSTRAINT FK_Asegurados_TO_Poliza
    FOREIGN KEY (DNI_Asegurado)
    REFERENCES Asegurados (DNI_Asegurado)
GO

ALTER TABLE Poliza
  ADD CONSTRAINT FK_Beneficiario_TO_Poliza
    FOREIGN KEY (Dni_beneficiario)
    REFERENCES Beneficiario (Dni_beneficiario)
GO

ALTER TABLE Poliza
  ADD CONSTRAINT FK_Agente_TO_Poliza
    FOREIGN KEY (Codigo_Agente)
    REFERENCES Agente (Codigo_Agente)
GO

ALTER TABLE Agente
  ADD CONSTRAINT FK_Broker_TO_Agente
    FOREIGN KEY (Codigo_Broker)
    REFERENCES Broker (Codigo_Broker)
GO

ALTER TABLE Poliza
  ADD CONSTRAINT FK_Pago_TO_Poliza
    FOREIGN KEY (PagoID)
    REFERENCES Pago (PagoID)
GO