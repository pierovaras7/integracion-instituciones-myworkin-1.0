from app.domain.model.student import Student

def ulima_to_domain(dto: dict) -> Student:
    full_name_parts = [
        dto.get("firstName"),
        dto.get("middleName"),
        dto.get("lastName"),
        dto.get("secondLastName"),
    ]
    fullName = " ".join([p for p in full_name_parts if p])

    return Student(
        id=dto.get("id"),
        displayName=dto.get("displayName"),
        fullName=fullName,
        firstName=dto.get("firstName"),
        middleName=dto.get("middleName"),
        lastName=dto.get("lastName"),
        secondLastName=dto.get("secondLastName"),
        email=dto.get("email"),
        phone=dto.get("phone"),
        birthdate=dto.get("birthdate"),
        gender=dto.get("gender"),
        discapacidad=dto.get("discapacidad"),
        alumni=dto.get("alumni"),
        schoolStudentId=dto.get("schoolStudentId"),
        coPers=dto.get("coPers"),
        coIdPs=dto.get("coIdPs"),
        role=dto.get("role") or "student",
        status=dto.get("status") or "active",
        university=dto.get("university"),
        verified=dto.get("verified", False),
        hasCV=dto.get("hasCV", False),
        usoPrimerHerramienta=dto.get("usoPrimerHerramienta", False),
        createdAt=dto.get("createdAt"),
        updatedAt=dto.get("updatedAt"),
        image=dto.get("image"),
        # Document fields
        tipoDocumento=dto.get("document", {}).get("tipoDocumento"),
        numeroDocumento=dto.get("document", {}).get("numeroDocumento"),
        paisEmisionDocumento=dto.get("document", {}).get("paisEmisionDocumento"),
        # Address fields
        street=dto.get("address", {}).get("street"),
        city=dto.get("address", {}).get("city"),
        dependentLocality=dto.get("address", {}).get("dependentLocality"),
        state=dto.get("address", {}).get("state"),
        zip=dto.get("address", {}).get("zip"),
        country=dto.get("address", {}).get("country"),
        # Contact fields
        emailUniversity=dto.get("contact", {}).get("emailUniversity"),
        emailAlternativo=dto.get("contact", {}).get("emailAlternativo"),
        telefonoAlternativo=dto.get("contact", {}).get("telefonoAlternativo"),
        # Academic fields
        applicantType=dto.get("academic", {}).get("applicantType"),
        degreeLevel=dto.get("academic", {}).get("degreeLevel"),
        degreeMode=dto.get("academic", {}).get("degreeMode"),
        degreeAward=dto.get("academic", {}).get("degreeAward"),
        degreeYear=dto.get("academic", {}).get("degreeYear"),
        degreePrimary=dto.get("academic", {}).get("degreePrimary"),
        degree=dto.get("academic", {}).get("degree"),
        subjectArea=dto.get("academic", {}).get("subjectArea"),
        institucionEducacionSuperior=dto.get("academic", {}).get("institucionEducacionSuperior"),
        rankingUlima=dto.get("academic", {}).get("rankingUlima"),
        ppa=dto.get("academic", {}).get("ppa"),
        cicloUltimaMatricula=dto.get("academic", {}).get("cicloUltimaMatricula"),
        creditosAprobados=dto.get("academic", {}).get("creditosAprobados"),
        creditosMatriculados=dto.get("academic", {}).get("creditosMatriculados"),
        fechaEgreso=dto.get("academic", {}).get("fechaEgreso"),
        # Studies
        tienesColegiatura=dto.get("studies", {}).get("tienesColegiatura"),
        tienesMaestria=dto.get("studies", {}).get("tienesMaestria"),
        tienesMaestriaExternaUl=dto.get("studies", {}).get("tienesMaestriaExternaUl"),
        # Preferences
        languages=dto.get("preferences", {}).get("languages"),
        receiveJobBlastEmail=dto.get("preferences", {}).get("receiveJobBlastEmail"),
        experientialLearning=dto.get("preferences", {}).get("experientialLearning"),
        # Rights
        canApplyJobs=dto.get("rights", {}).get("canApplyJobs"),
        canDownloadCertificates=dto.get("rights", {}).get("canDownloadCertificates"),
        canEditProfile=dto.get("rights", {}).get("canEditProfile"),
        # Laboral
        situacionLaboral=dto.get("situacionLaboral"),
        interesesLaborales=dto.get("interesesLaborales") or []
    )
