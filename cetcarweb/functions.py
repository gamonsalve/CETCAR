from .models import Servicio

def LlenarServicios():
	#ST=Servicio Técnico, S=Seguridad
	servicios=[("Instalación de sistema operativo","ST"),
				("Instalación, configuración y ejecución de antivirus","ST"),
				("Instalación y configuración de software varios","ST"),
				("Actualización y/o instalación de partes para computadores","ST"),
				("Instalación y configuración de periféricos y accesorios en general","ST"),
				("Mantenimiento preventivo de computadores y portstiles","ST"),
				("Mantenimiento preventivo de equipos de oficina en general","ST"),
				("Reparación de computadores y portatiles","ST"),
				("Reparación de equipos de oficina en general","ST"),
				("Reparación de servidores","ST"),
				("Intalación de cámaras de seguridad (IP y análogas)","S"),
				("Configuración de DVR","S"),]
	for i in range(0,len(servicios)):
		s=Servicio(id=i+1,nombre=servicios[i][0],categoria=servicios[i][1])
		s.save()
