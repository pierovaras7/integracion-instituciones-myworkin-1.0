from dataclasses import dataclass
from typing import Optional, List
from datetime import datetime


@dataclass
class Student:
    # Identidad
    id: Optional[str] = None
    displayName: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    firstName: Optional[str] = None
    middleName: Optional[str] = None
    lastName: Optional[str] = None
    secondLastName: Optional[str] = None
    fullName: Optional[str] = None
    image: Optional[str] = None
    birthdate: Optional[str] = None
    gender: Optional[str] = None
    discapacidad: Optional[bool] = None
    alumni: Optional[bool] = None

    # Estado de la cuenta
    role: Optional[str] = None
    status: Optional[str] = None
    university: Optional[str] = None
    verified: Optional[bool] = None
    hasCV: Optional[bool] = None
    usoPrimerHerramienta: Optional[bool] = None

    # Onboarding
    onboarding_completed: Optional[bool] = None
    onboarding_skipped: Optional[bool] = None
    onboarding_skippedAt: Optional[datetime] = None

    # Fechas Firebase
    createdAt: Optional[datetime] = None
    updatedAt: Optional[datetime] = None

    # Identificadores internos
    schoolStudentId: Optional[str] = None
    coPers: Optional[str] = None
    coIdPs: Optional[str] = None

    # Documentos
    tipoDocumento: Optional[str] = None
    numeroDocumento: Optional[str] = None
    paisEmisionDocumento: Optional[str] = None

    # Dirección
    street: Optional[str] = None
    city: Optional[str] = None
    dependentLocality: Optional[str] = None
    state: Optional[str] = None
    zip: Optional[str] = None
    country: Optional[str] = None

    # Información académica
    applicantType: Optional[str] = None
    degreeLevel: Optional[str] = None
    degreeMode: Optional[str] = None
    degreeAward: Optional[str] = None
    degreeYear: Optional[str] = None
    degreePrimary: Optional[bool] = None
    degree: Optional[str] = None
    subjectArea: Optional[str] = None
    institucionEducacionSuperior: Optional[str] = None
    rankingUlima: Optional[str] = None
    ppa: Optional[str] = None
    cicloUltimaMatricula: Optional[str] = None
    creditosAprobados: Optional[str] = None
    creditosMatriculados: Optional[str] = None
    fechaEgreso: Optional[str] = None

    # Estudios
    tienesColegiatura: Optional[bool] = None
    tienesMaestria: Optional[bool] = None
    tienesMaestriaExternaUl: Optional[bool] = None

    # Preferencias
    languages: Optional[List[str]] = None
    receiveJobBlastEmail: Optional[bool] = None
    experientialLearning: Optional[bool] = None

    # Derechos
    canApplyJobs: Optional[bool] = None
    canDownloadCertificates: Optional[bool] = None
    canEditProfile: Optional[bool] = None

    # Laboral
    situacionLaboral: Optional[str] = None
    interesesLaborales: Optional[List[str]] = None
