from typing import Optional, List, Dict
from datetime import date
from pydantic import BaseModel, EmailStr

class StudentULimaDTO(BaseModel):
    # 🔑 Identidad
    id: str
    firstName: str
    middleName: Optional[str] = None
    lastName: str
    secondLastName: Optional[str] = None
    fullName: Optional[str] = None
    image: Optional[str] = None

    birthdate: Optional[date] = None
    gender: Optional[str] = None
    discapacidad: Optional[bool] = None
    alumni: Optional[bool] = None

    # 🪪 Documento
    tipoDocumento: Optional[str] = None
    numeroDocumento: Optional[str] = None
    paisEmisionDocumento: Optional[str] = None
    schoolStudentId: Optional[str] = None
    coPers: Optional[str] = None
    coIdPs: Optional[str] = None

    # 📍 Contacto / Dirección
    street: Optional[str] = None
    city: Optional[str] = None
    dependentLocality: Optional[str] = None
    state: Optional[str] = None
    zip: Optional[str] = None
    country: Optional[str] = None

    email: EmailStr
    emailUniversity: Optional[EmailStr] = None
    emailAlternativo: Optional[EmailStr] = None
    phone: Optional[str] = None
    telefonoAlternativo: Optional[str] = None

    # 💼 Situación laboral
    situacionLaboral: Optional[str] = None  # "1","2","3","4"
    interesesLaborales: Optional[List[str]] = None

    # 🎓 Académico
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
    fechaEgreso: Optional[date] = None

    # 🎓 Formación adicional
    tienesColegiatura: Optional[bool] = None
    tienesMaestria: Optional[bool] = None
    tienesMaestriaExternaUl: Optional[bool] = None

    # 🌍 Idiomas
    languages: Optional[List[str]] = None

    # ⚙️ Preferencias
    receiveJobBlastEmail: Optional[bool] = None
    experientialLearning: Optional[bool] = None

    # 🔐 Derechos
    rights: Optional[Dict[str, bool]] = None

    class Config:
        extra = "ignore"
