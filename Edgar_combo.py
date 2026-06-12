import os
import datetime
import time
from colorama import Fore, Back, Style, init
import shutil
import urllib.request
import json
import unicodedata
import subprocess
import random
import sys
from tqdm import tqdm
import names
import string
from unidecode import unidecode

# Inicializar colorama
init(autoreset=True)

# Banner elegante con EDGAR como creador
print(Fore.CYAN + """
╔══════════════════════════════════════════════════════════╗
║                                                          ║
║           ███████╗██████╗   ██████╗  █████╗ ██████╗     ║
║           ██╔════╝██╔══██╗ ██╔════╝ ██╔══██╗██╔══██╗    ║
║           █████╗  ██║  ██║ ██║  ███╗███████║██████╔╝    ║
║           ██╔══╝  ██║  ██║ ██║   ██║██╔══██║██╔══██╗    ║
║           ███████╗██████╔╝ ╚██████╔╝██║  ██║██║  ██║    ║
║           ╚══════╝╚═════╝   ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝    ║
║                                                          ║
║            🚀 GENERADOR MÚLTIPLE DE COMBOS 🚀            ║
║               📡 MULTI HERRAMIENTAS DE IPTV 📡           ║
║                                                          ║
║                   👤 Creado por EDGAR                    ║
║                                                          ║
╚══════════════════════════════════════════════════════════╝
""" + Style.RESET_ALL)

simbolos = ['!', '@', '#', '$', '%']
dominios = ['gmail.com', 'hotmail.com', 'outlook.com']

def obtener_nombre_apellido(capitalize_option):
    try:
        url = 'https://randomuser.me/api/'
        response = urllib.request.urlopen(url)
        data = json.loads(response.read().decode())
        if not data['results']:
            return None, None
        nombre = unidecode(data['results'][0]['name']['first'])
        apellido = unidecode(data['results'][0]['name']['last'])
        
        nombre = nombre.replace("'", "").replace(" ", "")
        apellido = apellido.replace("'", "").replace(" ", "")
        
        if capitalize_option == '4':
            capitalize_option = random.choice(['1', '2', '3'])
        
        if capitalize_option == '1':
            nombre = nombre.lower()
            apellido = apellido.lower()
        elif capitalize_option == '2':
            nombre = nombre.capitalize()
            apellido = apellido.capitalize()
        elif capitalize_option == '3':
            nombre = nombre.upper()
            apellido = apellido.upper()
        
        return nombre, apellido
    except Exception as e:
        print(f"{Fore.RED}❌ Error al obtener datos de la API: {e}. Saltando este correo...{Style.RESET_ALL}")
        return None, None

def generar_fecha_nacimiento():
    year = random.randint(1900, 2050)
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    return year, f"{year}{month:02d}{day:02d}"

def generar_correo_contrasena(dominio_seleccionado, capitalize_option, email_number_option, password_number_option, name_option, use_symbols, first_letter_option):
    nombre, apellido = obtener_nombre_apellido(capitalize_option)
    
    if nombre is None or apellido is None:
        return None
    
    year, _ = generar_fecha_nacimiento()
    
    if dominio_seleccionado == 'todos':
        dominio = random.choice(dominios)
    else:
        dominio = dominio_seleccionado
    
    if email_number_option == '3':
        email_number_choice = random.choice(['1', '2', '4'])
    else:
        email_number_choice = email_number_option
    
    if email_number_choice == '1':
        numero_correo = str(year)
    elif email_number_choice == '2':
        numero_correo = str(random.randint(10, 99))
    else:
        numero_correo = ''
    
    if name_option == '4':
        name_choice = random.choice(['nombre', 'apellido', 'ambos'])
    else:
        name_choice = {'1': 'nombre', '2': 'apellido', '3': 'ambos'}[name_option]
    
    if name_choice == 'nombre':
        correo = f"{nombre}{numero_correo}@{dominio}"
    elif name_choice == 'apellido':
        correo = f"{apellido}{numero_correo}@{dominio}"
    else:
        correo = f"{nombre}{apellido}{numero_correo}@{dominio}"
    
    correo = correo.replace("'", "")
    
    if password_number_option == '3':
        password_number_choice = random.choice(['1', '2', '4'])
    else:
        password_number_choice = password_number_option
    
    if password_number_choice == '1':
        numero_contrasena = str(year)
    elif password_number_choice == '2':
        numero_contrasena = str(random.randint(1000, 9999))
    else:
        numero_contrasena = ''
    
    if first_letter_option == '3':
        first_letter_choice = random.choice(['1', '2'])
    else:
        first_letter_choice = first_letter_option
    
    if first_letter_choice == '1':
        nombre_contrasena = nombre.lower()
    else:
        nombre_contrasena = nombre.capitalize()
    
    nombre_contrasena = nombre_contrasena.replace(" ", "").replace("'", "")
    
    if use_symbols == '1':
        simbolo = random.choice(simbolos)
        contrasena = f"{nombre_contrasena}{numero_contrasena}{simbolo}"
    else:
        contrasena = f"{nombre_contrasena}{numero_contrasena}"
    
    contrasena = contrasena.replace("'", "")
    
    return f"{correo}:{contrasena}"

def generador_correos():
    print(f'\n{Fore.YELLOW}+------------------------------------+{Style.RESET_ALL}')
    print(f"{Fore.GREEN}📧 Generador de correos electrónicos 📧{Style.RESET_ALL}")
    print(f"{Fore.CYAN}1. Gmail")
    print("2. Hotmail")
    print("3. Outlook")
    print("4. Todos")
    print(f'{Fore.YELLOW}+------------------------------------+{Style.RESET_ALL}')

    opcion = input(f"\n{Fore.GREEN}🔢 Opción (1-4): {Style.RESET_ALL}")

    if opcion == '1':
        dominio = 'gmail.com'
    elif opcion == '2':
        dominio = 'hotmail.com'
    elif opcion == '3':
        dominio = 'outlook.com'
    elif opcion == '4':
        dominio = 'todos'
    else:
        print(f"{Fore.RED}❌ Opción inválida, usando 'todos' por defecto.{Style.RESET_ALL}")
        dominio = 'todos'
    
    print(f'\n{Fore.YELLOW}+------------------------------------+{Style.RESET_ALL}')
    print(f"{Fore.GREEN}🔤 Nombres y apellidos:{Style.RESET_ALL}")
    print("1. Todo en minúsculas")
    print("2. Primera letra en mayúscula")
    print("3. Todo en mayúsculas")
    print("4. Mezclar todos")
    print(f'{Fore.YELLOW}+------------------------------------+{Style.RESET_ALL}')
    capitalize_option = input(f"\n{Fore.GREEN}🔢 Opción (1-4): {Style.RESET_ALL}")
    
    if capitalize_option not in ['1', '2', '3', '4']:
        print(f"{Fore.RED}❌ Opción inválida, usando minúsculas por defecto.{Style.RESET_ALL}")
        capitalize_option = '1'
    
    print(f'\n{Fore.YELLOW}+------------------------------------+{Style.RESET_ALL}')
    print(f"{Fore.GREEN}🔢 Usar números en el correo:{Style.RESET_ALL}")
    print("1. Usar año de nacimiento")
    print("2. Usar números aleatorios")
    print("3. Mezclar todos")
    print("4. No usar nada")
    print(f'{Fore.YELLOW}+------------------------------------+{Style.RESET_ALL}')
    email_number_option = input(f"\n{Fore.GREEN}🔢 Opción (1-4): {Style.RESET_ALL}")
    
    if email_number_option not in ['1', '2', '3', '4']:
        print(f"{Fore.RED}❌ Opción inválida, usando números aleatorios por defecto.{Style.RESET_ALL}")
        email_number_option = '2'
    
    print(f'\n{Fore.YELLOW}+------------------------------------+{Style.RESET_ALL}')
    print(f"{Fore.GREEN}🔐 Opciones para contraseña:{Style.RESET_ALL}")
    print("1. Usar año de nacimiento")
    print("2. Usar números aleatorios")
    print("3. Mezclar todos")
    print("4. No usar nada")
    print(f'{Fore.YELLOW}+------------------------------------+{Style.RESET_ALL}')
    password_number_option = input(f"\n{Fore.GREEN}🔢 Opción (1-4): {Style.RESET_ALL}")
    
    if password_number_option not in ['1', '2', '3', '4']:
        print(f"{Fore.RED}❌ Opción inválida, usando números aleatorios por defecto.{Style.RESET_ALL}")
        password_number_option = '2'

    print(f'\n{Fore.YELLOW}+------------------------------------+{Style.RESET_ALL}')
    print(f"{Fore.GREEN}🔤 Primera letra de la contraseña:{Style.RESET_ALL}")
    print("1. Minúscula")
    print("2. Mayúscula")
    print("3. Mezclar ambas")
    print(f'{Fore.YELLOW}+------------------------------------+{Style.RESET_ALL}')
    first_letter_option = input(f"\n{Fore.GREEN}🔢 Opción (1-3): {Style.RESET_ALL}")
    
    if first_letter_option not in ['1', '2', '3']:
        print(f"{Fore.RED}❌ Opción inválida, usando minúscula por defecto.{Style.RESET_ALL}")
        first_letter_option = '1'
    
    print(f'\n{Fore.YELLOW}+------------------------------------+{Style.RESET_ALL}')
    print(f"{Fore.GREEN}✨ Usar símbolos en la contraseña:{Style.RESET_ALL}")
    print("1. Usar símbolos")
    print("2. No usar símbolos")
    print(f'{Fore.YELLOW}+------------------------------------+{Style.RESET_ALL}')
    use_symbols = input(f"\n{Fore.GREEN}🔢 Opción (1-2): {Style.RESET_ALL}")
    
    if use_symbols not in ['1', '2']:
        print(f"{Fore.RED}❌ Opción inválida, no se usarán símbolos por defecto.{Style.RESET_ALL}")
        use_symbols = '2'
    
    print(f'\n{Fore.YELLOW}+------------------------------------+{Style.RESET_ALL}')
    print(f"{Fore.GREEN}📝 Opciones para el correo:{Style.RESET_ALL}")
    print("1. Solo nombre")
    print("2. Solo apellido")
    print("3. Nombre y apellido")
    print("4. Todos")
    print(f'{Fore.YELLOW}+------------------------------------+{Style.RESET_ALL}')
    name_option = input(f"\n{Fore.GREEN}🔢 Opción (1-4): {Style.RESET_ALL}")
    
    if name_option not in ['1', '2', '3', '4']:
        print(f"{Fore.RED}❌ Opción inválida, usando 'Nombre y apellido' por defecto.{Style.RESET_ALL}")
        name_option = '3'
    
    try:
        cantidad = int(input(f"\n{Fore.GREEN}🔢 ¿Cuántos correos desea generar?: {Style.RESET_ALL}"))
        nombre_archivo = input(f"\n{Fore.GREEN}📝 Ingrese el nombre del archivo: {Style.RESET_ALL}") + ".txt"
    except ValueError:
        print(f"{Fore.RED}❌ Cantidad inválida, se generarán 10 correos por defecto.{Style.RESET_ALL}")
        cantidad = 10
        nombre_archivo = "correos_generados.txt"
    
    carpeta = "/storage/emulated/0/Combo/"
    ruta = os.path.join(carpeta, nombre_archivo)
    
    try:
        os.makedirs(carpeta, exist_ok=True)
    except Exception as e:
        print(f"{Fore.RED}❌ Error al crear la carpeta: {e}{Style.RESET_ALL}")
        return
    
    correos_generados = 0
    intentos = 0
    max_intentos = cantidad * 3
    
    try:
        with open(ruta, 'w', encoding='utf-8') as archivo:
            with tqdm(total=cantidad, desc="Generando correos", unit="correo") as pbar:
                while correos_generados < cantidad and intentos < max_intentos:
                    linea = generar_correo_contrasena(dominio, capitalize_option, email_number_option, password_number_option, name_option, use_symbols, first_letter_option)
                    intentos += 1
                    if linea:
                        archivo.write(linea + '\n')
                        correos_generados += 1
                        pbar.update(1)
                    time.sleep(0.1)
        print(f"\n{Fore.GREEN}✅ Se han generado {correos_generados} correos y guardado en {ruta}{Style.RESET_ALL}")
        if correos_generados < cantidad:
            print(f"{Fore.YELLOW}⚠️ Advertencia: Solo se generaron {correos_generados} de {cantidad} correos solicitados.{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}❌ Error al guardar el archivo: {e}{Style.RESET_ALL}")

def generar_combinaciones(nombres_archivo, combos_archivo):
    try:
        with open(nombres_archivo, 'r', encoding='utf-8') as f:
            nombres = [nombre.strip() for nombre in f if nombre.strip()]
    except Exception as e:
        print(f"{Fore.RED}❌ Error leyendo archivo de nombres: {e}{Style.RESET_ALL}")
        return [], 0, 0

    try:
        with open(combos_archivo, 'r', encoding='utf-8') as f:
            combos = [combo.strip() for combo in f if combo.strip()]
    except Exception as e:
        print(f"{Fore.RED}❌ Error leyendo archivo de combinaciones: {e}{Style.RESET_ALL}")
        return [], 0, 0

    resultados = []
    num_omitidas = 0
    for nombre in nombres:
        for combo in combos:
            resultado = combo.replace('usuario', nombre)
            if 'usuario' in resultado:
                num_omitidas += 1
            else:
                resultados.append(resultado)

    num_combinaciones = len(resultados)
    return resultados, num_combinaciones, num_omitidas

def remove_accents(text):
    return ''.join(c for c in unicodedata.normalize('NFD', text)
                   if unicodedata.category(c) != 'Mn')

def get_names(gender, quantity):
    if gender == 'both':
        url = f"https://randomuser.me/api/?results={quantity}&nat=us,es,fr,gb"
    else:
        url = f"https://randomuser.me/api/?results={quantity}&gender={gender}&nat=us,es,fr,gb"
    
    try:
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read().decode())
            return [(remove_accents(user['name']['first']), 
                     remove_accents(user['name']['last'])) 
                    for user in data['results']]
    except Exception as e:
        print(f"{Fore.RED}❌ Error al obtener nombres: {e}{Style.RESET_ALL}")
        return []

def format_name(name, case_option):
    if case_option == 'upper':
        return name.capitalize()
    elif case_option == 'lower':
        return name.lower()
    else:
        return random.choice([name.capitalize(), name.lower()])

def format_output(first_name, last_name, case_option, output_type, combo_option='both'):
    formatted_first = format_name(first_name, case_option)
    formatted_last = format_name(last_name, case_option)
    
    if output_type == 'first':
        return [formatted_first]
    elif output_type == 'last':
        return [formatted_last]
    else:
        if combo_option == 'first_last':
            return [f"{formatted_first}{formatted_last}"]
        elif combo_option == 'last_first':
            return [f"{formatted_last}{formatted_first}"]
        else:
            return [f"{formatted_first}{formatted_last}", f"{formatted_last}{formatted_first}"]

def print_green_box(title, options):
    fixed_width = 38
    title = (title[:fixed_width-1] + '…') if len(title) > fixed_width else title.ljust(fixed_width)
    print(f"{Fore.GREEN}┌{'─' * (fixed_width + 2)}┐{Style.RESET_ALL}")
    print(f"{Fore.GREEN}│ {Fore.YELLOW}{title}{Fore.GREEN} │{Style.RESET_ALL}")
    print(f"{Fore.GREEN}├{'─' * (fixed_width + 2)}┤{Style.RESET_ALL}")
    for opt in options:
        opt = (opt[:fixed_width-1] + '…') if len(opt) > fixed_width else opt.ljust(fixed_width)
        print(f"{Fore.GREEN}│ {opt} │{Style.RESET_ALL}")
    print(f"{Fore.GREEN}└{'─' * (fixed_width + 2)}┘{Style.RESET_ALL}")

def progress_bar(seconds):
    bar_length = 40
    for i in range(100):
        time.sleep(seconds/100)
        if i < 33:
            print(f"\r{Fore.RED}[{'●' * round(i*bar_length//100)}{'-' * (bar_length - round(i*bar_length//100))}]{Style.RESET_ALL}", end="", flush=True)
        elif i < 66:
            print(f"\r{Fore.YELLOW}[{'●' * round(i*bar_length//100)}{'-' * (bar_length - round(i*bar_length//100))}]{Style.RESET_ALL}", end="", flush=True)
        else:
            print(f"\r{Fore.GREEN}[{'●' * round(i*bar_length//100)}{'-' * (bar_length - round(i*bar_length//100))}]{Style.RESET_ALL}", end="", flush=True)
    print(f"\r{Fore.GREEN}[{'●' * bar_length}]{Style.RESET_ALL}")
    print(f"{Fore.GREEN}✅ Proceso terminado{Style.RESET_ALL}")

def generador_nombres():
    gender_options = {'1': 'male', '2': 'female', '3': 'both'}
    print_green_box("Opciones de género disponibles:", ["1. Hombre 👨", "2. Mujer 👩", "3. Ambos 👥"])
    gender_choice = input(f"\n{Fore.GREEN}🔢 Seleccione género (1, 2, 3): {Style.RESET_ALL}")
    while gender_choice not in gender_options:
        print(f"{Fore.RED}❌ Opción inválida. Use 1, 2 o 3.{Style.RESET_ALL}")
        gender_choice = input(f"{Fore.GREEN}🔢 Seleccione género (1, 2, 3): {Style.RESET_ALL}")
    gender = gender_options[gender_choice]

    try:
        quantity = int(input(f"\n{Fore.YELLOW}🔢 Cantidad de nombres a generar:{Style.RESET_ALL} "))
        if quantity <= 0:
            raise ValueError("La cantidad debe ser mayor que 0.")
    except ValueError as e:
        print(f"{Fore.RED}❌ Error: {e if str(e) else 'Ingrese un número válido.'}{Style.RESET_ALL}")
        return

    case_options = {'1': 'upper', '2': 'lower', '3': 'both'}
    print_green_box("Formato de la primera letra:", ["1. Mayúscula 🔠", "2. Minúscula 🔡", "3. Ambas 🔀"])
    case_choice = input(f"\n{Fore.GREEN}🔢 Seleccione formato (1, 2, 3): {Style.RESET_ALL}")
    while case_choice not in case_options:
        print(f"{Fore.RED}❌ Opción inválida. Use 1, 2 o 3.{Style.RESET_ALL}")
        case_choice = input(f"{Fore.GREEN}🔢 Seleccione formato (1, 2, 3): {Style.RESET_ALL}")
    case_option = case_options[case_choice]

    output_options = {'1': 'first', '2': 'last', '3': 'combo'}
    print_green_box("Combinación de nombres o apellidos:", ["1. Solo nombres 👤", "2. Solo apellidos 👥", "3. Ambos 🔄"])
    output_choice = input(f"\n{Fore.GREEN}🔢 Seleccione (1, 2, 3): {Style.RESET_ALL}")
    while output_choice not in output_options:
        print(f"{Fore.RED}❌ Opción inválida. Use 1, 2 o 3.{Style.RESET_ALL}")
        output_choice = input(f"{Fore.GREEN}🔢 Seleccione (1, 2, 3): {Style.RESET_ALL}")
    output_type = output_options[output_choice]

    combo_option = 'both'
    if output_type == 'combo':
        combo_options = {'1': 'first_last', '2': 'last_first', '3': 'both'}
        print_green_box("Combinación con nombres y apellidos:", ["1. Nombre/Apellido 📝", "2. Apellido/Nombre 📝", "3. Ambas 🔄"])
        combo_choice = input(f"\n{Fore.GREEN}🔢 Seleccione combinación (1, 2, 3): {Style.RESET_ALL}")
        while combo_choice not in combo_options:
            print(f"{Fore.RED}❌ Opción inválida. Use 1, 2 o 3.{Style.RESET_ALL}")
            combo_choice = input(f"{Fore.GREEN}🔢 Seleccione combinación (1, 2, 3): {Style.RESET_ALL}")
        combo_option = combo_options[combo_choice]

    file_name = input(f"\n{Fore.GREEN}📝 Nombre para guardar el archivo (sin .txt): {Style.RESET_ALL}").strip()
    if not file_name:
        file_name = "nombres_generados"
    file_name += ".txt"

    print(f"\n{Fore.CYAN}🔄 Procesando nombres...{Style.RESET_ALL}")
    progress_bar(5)

    names_list = get_names(gender, quantity)
    if not names_list:
        print(f"\n{Fore.RED}❌ No se pudieron obtener nombres. Finalizando.{Style.RESET_ALL}")
        return

    formatted_names = []
    for first_name, last_name in names_list:
        result = format_output(first_name, last_name, case_option, output_type, combo_option)
        formatted_names.extend(result)

    output_dir = "/storage/emulated/0/Combo/"
    try:
        os.makedirs(output_dir, exist_ok=True)
    except Exception as e:
        print(f"{Fore.RED}❌ Error al crear la carpeta {output_dir}: {e}{Style.RESET_ALL}")
        return

    output_path = os.path.join(output_dir, file_name)
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            for name in formatted_names:
                f.write(name + '\n')
        print(f"\n{Fore.GREEN}✅ Nombres guardados en: {output_path}{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}❌ Error al guardar el archivo: {e}{Style.RESET_ALL}")

def generar_combo(rname, rlastname, num, combo_option):
    if combo_option == "1":
        all1 = f"{rname}{num}"
        alln = f"{all1}:{rname}"
        all2 = f"{rlastname}{num}"
        allf = f"{all2}:{rlastname}"
    elif combo_option == "2":
        all1 = f"{rname}"
        alln = f"{all1}:{rname}{num}"
        all2 = f"{rlastname}"
        allf = f"{all2}:{rlastname}{num}"
    else:
        all1 = f"{rname}{num}"
        alln = f"{all1}:{rname}{num}"
        all2 = f"{rlastname}{num}"
        allf = f"{all2}:{rlastname}{num}"
    return all1, alln, all2, allf

def generate_random_combos(user_length, pass_length, include_uppercase=True, include_lowercase=True, numbers=True, birth_year=False, year_position='right'):
    charset = ''
    if include_uppercase:
        charset += string.ascii_uppercase
    if include_lowercase:
        charset += string.ascii_lowercase
    if numbers and not birth_year:
        charset += string.digits
    if not charset:
        charset = string.ascii_lowercase

    username = ''.join(random.choice(charset) for _ in range(user_length))
    password = ''.join(random.choice(charset) for _ in range(pass_length))

    if birth_year:
        year = str(random.randint(1900, 2020))
        if year_position == 'left':
            username = username + year
        elif year_position == 'right':
            password = password + year
        elif year_position == 'both':
            username = username + year
            password = password + year
    return username, password

def generador_combos():
    output_dir = "/storage/emulated/0/Combo/"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    print(f'\n{Fore.YELLOW}+--------------------------------------+{Style.RESET_ALL}')
    print(f"{Fore.YELLOW}|{Style.RESET_ALL}{Fore.CYAN}      Menú de generador de Combos     {Style.RESET_ALL}{Fore.YELLOW}|{Style.RESET_ALL}")
    print(f'{Fore.YELLOW}+--------------------------------------+{Style.RESET_ALL}')
    print(f"{Fore.YELLOW}|{Style.RESET_ALL}{Fore.GREEN}1.- User:Pass (Num. de 2000 a 2050)   {Fore.YELLOW}|{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}|{Style.RESET_ALL}{Fore.GREEN}2.- User:Pass (Nombre-Nombre)         {Fore.YELLOW}|{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}|{Style.RESET_ALL}{Fore.GREEN}3.- User:Pass (Núm. de 1 a 99)        {Fore.YELLOW}|{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}|{Style.RESET_ALL}{Fore.GREEN}4.- User:Pass (Núm. de 100 a 999)     {Fore.YELLOW}|{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}|{Style.RESET_ALL}{Fore.GREEN}5.- User:Pass (Alfanuméricos)         {Fore.YELLOW}|{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}|{Style.RESET_ALL}{Fore.GREEN}6.- User:Pass (Año de Nacimiento)     {Fore.YELLOW}|{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}|{Style.RESET_ALL}{Fore.GREEN}7.- User:Pass (2023 al 2028)          {Fore.YELLOW}|{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}|{Style.RESET_ALL}{Fore.GREEN}8.- User:Pass (Núm. de 111 a 999)     {Fore.YELLOW}|{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}|{Style.RESET_ALL}{Fore.GREEN}9.- User:Pass (Núm. de 123 a 12345)   {Fore.YELLOW}|{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}|{Style.RESET_ALL}{Fore.GREEN}10.- User:Numero (12345..Random)      {Fore.YELLOW}|{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}|{Style.RESET_ALL}{Fore.GREEN}11.- Combos numéricos (numero:número) {Fore.YELLOW}|{Style.RESET_ALL}")
    print(f'{Fore.YELLOW}+--------------------------------------+{Style.RESET_ALL}')

    menu = input(f"\n{Fore.GREEN}🔢 Ingrese su elección: {Style.RESET_ALL}")

    if menu == "11":
        RED = Fore.RED
        GREEN = Fore.GREEN
        YELLOW = Fore.YELLOW
        CYAN = Fore.CYAN
        RESET = Style.RESET_ALL

        EMOJI_PROGRESS = "🔄"
        EMOJI_DONE = "✅"
        EMOJI_STAR = "✨"

        def logo():
            print(f"{YELLOW}{EMOJI_STAR*3} combos numericos {EMOJI_STAR*3}\n{RESET}")

        def clear_line():
            sys.stdout.write("\r" + " " * 60 + "\r")
            sys.stdout.flush()

        def barra_progreso(actual, total):
            longitud_barra = 18
            porcentaje = actual / total
            cantidad_bloques = int(porcentaje * longitud_barra)
            barra = "■" * cantidad_bloques + "-" * (longitud_barra - cantidad_bloques)
            clear_line()
            sys.stdout.write(
                f"{CYAN}{EMOJI_PROGRESS} [{barra}] {actual}/{total} combos generados{RESET}"
            )
            sys.stdout.flush()

        def crear_combo(long_usuario, long_contra, modo_contra="random", contra_consec=None):
            usuario = "".join(random.choices("1234567890", k=long_usuario))
            if modo_contra == "consec":
                contra = contra_consec
            else:
                contra = "".join(random.choices("1234567890", k=long_contra))
            return f"{usuario}:{contra}"

        logo()

        try:
            total = int(input(f"{YELLOW}👉 ¿Cuántos combos quieres generar? {RESET} "))
            long_usuario = int(input(f"\n{YELLOW}😎 Longitud numérica para USUARIO: {RESET}"))

            print(f"\n{YELLOW}¿Qué tipo de contraseña quieres usar?{RESET}")
            print("1 - Consecutiva (ejemplo: 12345...)")
            print("2 - Aleatoria")
            print("3 - Ambos (mezclados)")
            opcion_contra = input("Elige opción (1, 2 o 3): ").strip()

            if opcion_contra not in ["1", "2", "3"]:
                print(f"{RED}❌ Opción inválida, usando aleatoria por defecto.{RESET}")
                opcion_contra = "2"

            long_contra = int(input(f"\n{YELLOW}🔑 Longitud numérica para CONTRASEÑA: {RESET} "))

            contra_consec = None
            if opcion_contra in ["1", "3"]:
                base = "123456789"
                veces = (long_contra // 10) + 1
                contra_consec = (base * veces)[:long_contra]

            nombre_archivo = input(f"\n{YELLOW}💾 Nombre del archivo: {RESET} ").strip()
            if not nombre_archivo:
                nombre_archivo = "combos_generados"
        except Exception:
            print(f"{RED}❌ Entrada inválida, por favor ingresa números válidos.{RESET}")
            return True

        ruta_archivo = os.path.join(output_dir, nombre_archivo + ".txt")

        with open(ruta_archivo, "w") as f:
            for i in range(1, total + 1):
                if opcion_contra == "1":
                    combo = crear_combo(long_usuario, long_contra, "consec", contra_consec)
                elif opcion_contra == "2":
                    combo = crear_combo(long_usuario, long_contra, "random")
                else:
                    if i % 2 == 0:
                        combo = crear_combo(long_usuario, long_contra, "consec", contra_consec)
                    else:
                        combo = crear_combo(long_usuario, long_contra, "random")

                f.write(combo + "\n")
                barra_progreso(i, total)
                time.sleep(0.01)

        clear_line()
        print(f"\n{GREEN}{EMOJI_DONE} ¡Listo! Se generaron {total} combos y se guardaron en: {ruta_archivo}{RESET}")
        return True

    if menu not in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]:
        print(f"{Fore.RED}❌ Opción no válida. Intente de nuevo.{Style.RESET_ALL}")
        return True

    filename = input(f"\n{Fore.GREEN}📝 Ingrese el nombre para su archivo de combo (sin .txt): {Style.RESET_ALL}")
    try:
        hwm = int(input(f"\n{Fore.YELLOW}🔢 Número de combos a generar:{Style.RESET_ALL} "))
        if hwm <= 0:
            raise ValueError("El número debe ser mayor que 0.")
    except ValueError as e:
        print(f"{Fore.RED}❌ Error: {e if str(e) else 'Ingrese un número válido.'}{Style.RESET_ALL}")
        return True

    combo_option = "3"
    if menu in ["1", "3", "4", "6", "7", "8"]:
        print(f"\n{Fore.YELLOW}🔢 Generar combinación:{Style.RESET_ALL}")
        print("1) Solo lado izquierdo")
        print("2) Solo lado derecho")
        print("3) Ambos lados")
        combo_option = input(f"\n{Fore.GREEN}🔢 Elija una opción: {Style.RESET_ALL}")
        if combo_option not in ["1", "2", "3"]:
            print(f"{Fore.RED}❌ Opción de combinación no válida. Usando ambos lados por defecto.{Style.RESET_ALL}")
            combo_option = "3"

    user_length = pass_length = 0
    include_uppercase = include_lowercase = numbers = False
    birth_year = False
    year_position = 'right'
    
    if menu == "5":
        print(f"\n{Fore.YELLOW}🔢 Generador de combos alfanuméricos{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}✨ Ideas KATYA ✨{Style.RESET_ALL}")

        print(f"\n{Fore.YELLOW}🔢 Selecciona el tipo de combo para generar:{Style.RESET_ALL}")
        print("1. Solo letras")
        print("2. Letras y números")
        print("3. Letras y año de nacimiento")
        try:
            option_type = int(input(f"\n{Fore.GREEN}🔢 Ingresa tu selección (1-3): {Style.RESET_ALL}"))
            if option_type not in [1, 2, 3]:
                raise ValueError("Selección inválida. Debe ser 1, 2 o 3.")
        except ValueError as e:
            print(f"{Fore.RED}❌ Error: {e}{Style.RESET_ALL}")
            return True

        try:
            user_length = int(input(f"\n{Fore.GREEN}🔢 Ingresa la longitud deseada para el usuario: {Style.RESET_ALL}"))
            pass_length = int(input(f"\n{Fore.GREEN}🔢 Ingresa la longitud deseada para la contraseña: {Style.RESET_ALL}"))
            if user_length <= 0 or pass_length <= 0:
                raise ValueError("Las longitudes deben ser mayores que 0.")
        except ValueError as e:
            print(f"{Fore.RED}❌ Error: {e}{Style.RESET_ALL}")
            return True

        if option_type == 3:
            print(f"\n{Fore.YELLOW}🔢 Selecciona dónde colocar el año de nacimiento:{Style.RESET_ALL}")
            print("1. Izquierda")
            print("2. Derecha")
            print("3. Ambos")
            try:
                year_option = int(input(f"\n{Fore.GREEN}🔢 Ingresa tu selección (1-3): {Style.RESET_ALL}"))
                if year_option not in [1, 2, 3]:
                    raise ValueError("Selección inválida. Debe ser 1, 2 o 3.")
                if year_option == 1:
                    year_position = 'left'
                elif year_option == 2:
                    year_position = 'right'
                elif year_option == 3:
                    year_position = 'both'
                birth_year = True
            except ValueError as e:
                print(f"{Fore.RED}❌ Error: {e}{Style.RESET_ALL}")
                return True

        print(f"\n{Fore.YELLOW}🔢 Selecciona las opciones para las letras:{Style.RESET_ALL}")
        print("1. Solo letras mayúsculas")
        print("2. Solo letras minúsculas")
        print("3. Ambas mayúsculas y minúsculas")
        try:
            option_case = int(input(f"\n{Fore.GREEN}🔢 Ingresa tu selección (1-3): {Style.RESET_ALL}"))
            if option_case not in [1, 2, 3]:
                raise ValueError("Selección inválida. Debe ser 1, 2 o 3.")
        except ValueError as e:
            print(f"{Fore.RED}❌ Error: {e}{Style.RESET_ALL}")
            return True

        if option_type == 1:
            numbers = False
        elif option_type == 2:
            numbers = True
        elif option_type == 3:
            numbers = False

        if option_case == 1:
            include_uppercase = True
        elif option_case == 2:
            include_lowercase = True
        elif option_case == 3:
            include_uppercase = True
            include_lowercase = True

    lines_set = set()
    output_file = os.path.join(output_dir, f"{filename}.txt")
    batch = []

    with tqdm(total=hwm, desc="Generando combos", unit="líneas",
              bar_format=Fore.GREEN + "{desc}" + Style.RESET_ALL + "\n{bar:20} {percentage:.1f}%\nTiempo estimado: {remaining_s:.1f}s",
              ascii="□■", smoothing=0.1) as pbar:
        while len(lines_set) < hwm:
            try:
                rname = names.get_first_name()
                rlastname = names.get_last_name()
            except:
                rname = "usuario" + str(random.randint(1000, 9999))
                rlastname = "apellido" + str(random.randint(1000, 9999))

            if menu == "1":
                num = random.randint(2000, 2050)
                all1, alln, all2, allf = generar_combo(rname, rlastname, num, combo_option)
            elif menu == "2":
                all1 = rname
                alln = f"{all1}:{rlastname}"
                all2 = rlastname
                allf = f"{all2}:{rname}"
            elif menu == "3":
                num = random.randint(1, 99)
                all1, alln, all2, allf = generar_combo(rname, rlastname, num, combo_option)
            elif menu == "4":
                num = random.randint(100, 999)
                all1, alln, all2, allf = generar_combo(rname, rlastname, num, combo_option)
            elif menu == "5":
                username, password = generate_random_combos(user_length, pass_length, include_uppercase, include_lowercase, numbers, birth_year, year_position)
                line = f"{username}:{password}\n"
                if line not in lines_set:
                    lines_set.add(line)
                    batch.append(line)
                    pbar.update(1)
                continue
            elif menu == "6":
                num = random.randint(1960, 2050)
                all1, alln, all2, allf = generar_combo(rname, rlastname, num, combo_option)
            elif menu == "7":
                num = random.choice(["2023", "2024", "2025", "2026", "2027", "2028"])
                all1, alln, all2, allf = generar_combo(rname, rlastname, num, combo_option)
            elif menu == "8":
                num = random.choice(["111", "222", "333", "444", "555", "666", "777", "888", "999"])
                all1, alln, all2, allf = generar_combo(rname, rlastname, num, combo_option)
            elif menu == "9":
                num = random.choice(["123", "1234", "12345", "321", "4321", "54321"])
                all1, alln, all2, allf = generar_combo(rname, rlastname, num, combo_option)
            elif menu == "10":
                numbers1 = random.choice(["123", "1234", "12345", "123456", "1234567", "12345678", "4321", "54321", "654321","102030"])
                numbers2 = random.choice(["123", "1234", "12345", "123456", "1234567", "12345678", "4321", "54321", "654321", "102030"])
                all1 = f"{rname}:{numbers1}"
                all2 = f"{rlastname}:{numbers2}"
                alln = all1
                allf = all2
            else:
                continue

            lines = [f"{alln}\n", f"{allf}\n"]
            random.shuffle(lines)
            for line in lines:
                if line not in lines_set and len(lines_set) < hwm:
                    lines_set.add(line)
                    batch.append(line)
                    pbar.update(1)
                    break

            if len(batch) >= 100:
                with open(output_file, "a+", encoding="utf-8") as f:
                    f.writelines(batch)
                batch = []

    if batch:
        with open(output_file, "a+", encoding="utf-8") as f:
            f.writelines(batch)

    print(f"\n{Fore.GREEN}✅ Archivo de combo guardado como: {output_file}{Style.RESET_ALL}")
    return True

def multifuncion_combos():
    def print_menu():
        print(f"\n{Fore.GREEN}🛠️ Python duplicas/unidor/divisor de combos{Style.RESET_ALL}\n")
        print(f"{Fore.YELLOW}╔══════════════════════════{Style.RESET_ALL}       ")
        print(f"{Fore.YELLOW}║{Style.RESET_ALL}     {Fore.CYAN}MENÚ MULTIFUNCIÓN{Style.RESET_ALL}   {Fore.YELLOW}║{Style.RESET_ALL}   ")
        print(f"{Fore.YELLOW}║{Style.RESET_ALL}1. Eliminar duplicados   {Fore.YELLOW}║{Style.RESET_ALL}     ")
        print(f"{Fore.YELLOW}║{Style.RESET_ALL}2. Unir combos           {Fore.YELLOW}║{Style.RESET_ALL}     ")
        print(f"{Fore.YELLOW}║{Style.RESET_ALL}3. Dividir archivos      {Fore.YELLOW}║{Style.RESET_ALL}    ")
        print(f"{Fore.YELLOW}║{Style.RESET_ALL}4. Salir                 {Fore.YELLOW}║{Style.RESET_ALL}     ")
        print(f"{Fore.YELLOW}╚══════════════════════════{Style.RESET_ALL}      ")

    def unir_combos():
        print(f"\n{Back.YELLOW}{Fore.BLACK} UNIR ARCHIVOS DE LA CARPETA 'Combo' {Style.RESET_ALL}")
        folder_path = '/storage/emulated/0/Combo'
        if not os.path.exists(folder_path):
            print(f"{Fore.RED}❌ La carpeta Combo no existe{Style.RESET_ALL}")
            return
        print(f"\n{Fore.CYAN}📁 Archivos disponibles en la carpeta:{Style.RESET_ALL}\n")
        files = [f for f in os.listdir(folder_path) if f.endswith('.txt')]
        if not files:
            print(f"{Fore.RED}❌ No hay archivos .txt en la carpeta{Style.RESET_ALL}")
            return
        for i, file in enumerate(files):
            print(f"{Fore.GREEN}{i+1}. {file}{Style.RESET_ALL}")
        selected_files = input(f"\n{Fore.GREEN}🔢 Selecciona los archivos que deseas unir (ingresa los números separados por comas): {Style.RESET_ALL}")
        selected_files_indices = [int(index) - 1 for index in selected_files.split(',')]
        total_lines = 0
        combined_lines = []
        for index in selected_files_indices:
            if index < len(files):
                file_path = os.path.join(folder_path, files[index])
                with open(file_path, 'r', encoding='utf-8') as file:
                    lines = file.readlines()
                    total_lines += len(lines)
                    combined_lines.extend(lines)
        unique_combined_lines = list(set(combined_lines))
        print(f"\n\n{Fore.GREEN}📊 Número de líneas originales en los archivos: {total_lines}{Style.RESET_ALL}")
        print(f"{Fore.GREEN}📊 Número de líneas en el archivo combinado: {len(unique_combined_lines)}{Style.RESET_ALL}")
        output_file_name = input(f"{Fore.GREEN}📝 Nombre para guardar los resultados: {Style.RESET_ALL}") + ".txt"
        output_file_path = os.path.join(folder_path, output_file_name)
        with open(output_file_path, 'w', encoding='utf-8') as file:
            file.writelines(unique_combined_lines)
        print(f"\n{Fore.GREEN}✅ Archivo guardado como '{output_file_name}'{Style.RESET_ALL}")

    def eliminar_duplicados_combos():
        print(f"\n{Back.YELLOW}{Fore.BLACK} ELIMINAR DUPLICADOS DE LOS COMBOS {Style.RESET_ALL}")
        folder_path = '/storage/emulated/0/Combo'
        if not os.path.exists(folder_path):
            print(f"{Fore.RED}❌ La carpeta Combo no existe{Style.RESET_ALL}")
            return
        print(f"\n{Fore.CYAN}📁 Archivos disponibles en la carpeta de combos:{Style.RESET_ALL}\n")
        files = [f for f in os.listdir(folder_path) if f.endswith('.txt')]
        if not files:
            print(f"{Fore.RED}❌ No hay archivos .txt en la carpeta{Style.RESET_ALL}")
            return
        for i, file in enumerate(files):
            print(f"{Fore.GREEN}{i + 1}. {file}{Style.RESET_ALL}")
        selected_file = int(input(f"\n{Fore.GREEN}🔢 Selecciona un archivo de combo (ingresa el número): {Style.RESET_ALL}")) - 1
        if selected_file >= len(files):
            print(f"{Fore.RED}❌ Selección inválida{Style.RESET_ALL}")
            return
        file_name = files[selected_file]
        file_path = os.path.join(folder_path, file_name)
        print(f"\n{Fore.CYAN}📖 Leyendo archivo {Fore.GREEN}'{file_name}'{Fore.CYAN} para quitar duplicados{Style.RESET_ALL}")
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        unique_lines = list(set(lines))
        num_duplicates = len(lines) - len(unique_lines)
        print(f"\n{Back.YELLOW}{Fore.BLACK} Resumen del archivo: '{file_name}'{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}---------------------------------------------{Style.RESET_ALL}")
        print(f"{Fore.GREEN}📄 Archivo que usaste: {file_name}{Style.RESET_ALL}")
        print(f"{Fore.GREEN}📊 Total de líneas: {len(lines)}{Style.RESET_ALL}")
        print(f"{Fore.GREEN}🔄 Número de líneas duplicadas: {num_duplicates}{Style.RESET_ALL}")
        print(f"{Fore.GREEN}✨ Número de líneas únicas: {len(unique_lines)}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}--------------------------------------------{Style.RESET_ALL}\n")
        output_file_name = input(f"{Fore.GREEN}📝 Nombre para guardar los resultados: {Style.RESET_ALL}") + ".txt"
        output_file_path = os.path.join(folder_path, output_file_name)
        with open(output_file_path, 'w', encoding='utf-8') as file:
            file.writelines(unique_lines)
        print(f"\n{Fore.GREEN}✅ Archivo guardado como '{output_file_name}'{Style.RESET_ALL}")

    def dividir_archivos():
        print(f"\n{Back.YELLOW}{Fore.BLACK} DIVIDIR ARCHIVOS EN VARIAS PARTES {Style.RESET_ALL}")
        folder_path = '/storage/emulated/0/Combo'
        if not os.path.exists(folder_path):
            print(f"{Fore.RED}❌ La carpeta Combo no existe{Style.RESET_ALL}")
            return
        print(f"\n{Fore.CYAN}📁 Archivos disponibles en la carpeta de combos:{Style.RESET_ALL}\n")
        files = [f for f in os.listdir(folder_path) if f.endswith('.txt')]
        if not files:
            print(f"{Fore.RED}❌ No hay archivos .txt en la carpeta{Style.RESET_ALL}")
            return
        for i, file in enumerate(files):
            print(f"{Fore.GREEN}{i + 1}. {file}{Style.RESET_ALL}")
        selected_file = int(input(f"\n{Fore.GREEN}🔢 Selecciona un archivo de combo para dividir (ingresa el número): {Style.RESET_ALL}")) - 1
        if selected_file >= len(files):
            print(f"{Fore.RED}❌ Selección inválida{Style.RESET_ALL}")
            return
        file_name = files[selected_file]
        file_path = os.path.join(folder_path, file_name)
        print(f"\n{Fore.CYAN}✂️ Dividiendo archivo {Fore.GREEN}'{file_name}'{Fore.CYAN} en varias partes{Style.RESET_ALL}")
        parts_number = int(input(f"\n{Fore.GREEN}🔢 ¿En cuántas partes quieres dividir el archivo?: {Style.RESET_ALL}"))
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        lines_per_part = len(lines) // parts_number
        if len(lines) % parts_number != 0:
            parts_number += 1
        print(f"\n{Fore.CYAN}✂️ Dividiendo archivo en {Fore.YELLOW}{parts_number}{Fore.CYAN} partes...{Style.RESET_ALL}")
        for i in range(parts_number):
            start_idx = i * lines_per_part
            end_idx = min((i + 1) * lines_per_part, len(lines))
            output_file_name = f"{file_name[:-4]}_parte_{i+1}.txt"
            output_file_path = os.path.join(folder_path, output_file_name)
            with open(output_file_path, 'w', encoding='utf-8') as output_file:
                output_file.writelines(lines[start_idx:end_idx])
        print(f"\n{Fore.GREEN}✅ Proceso de división de archivos terminado.{Style.RESET_ALL}")

    while True:
        print_menu()
        opcion = input(f"\n{Fore.GREEN}🔢 Selecciona una opción del menú: {Style.RESET_ALL}")
        if opcion == '1':
            eliminar_duplicados_combos()
        elif opcion == '2':
            unir_combos()
        elif opcion == '3':
            dividir_archivos()
        elif opcion == '4':
            print(f"{Fore.GREEN}👋 Saliendo del programa...{Style.RESET_ALL}")
            break
        else:
            print(f"{Fore.RED}❌ Opción no válida. Por favor, selecciona una opción válida.{Style.RESET_ALL}")

def menu_principal():
    carpetas = ['/storage/emulated/0/Resultados_combinaciones', '/storage/emulated/0/Combo']
    for carpeta in carpetas:
        if not os.path.exists(carpeta):
            os.makedirs(carpeta)

    while True:
        print(f'\n{Fore.YELLOW}+------------------------------------+{Style.RESET_ALL}')
        print(f'{Fore.YELLOW}|{Style.RESET_ALL}{Fore.CYAN}      Menú Principal de combos      {Style.RESET_ALL}{Fore.YELLOW}|{Style.RESET_ALL}')
        print(f'{Fore.YELLOW}--------------------------------------{Style.RESET_ALL}')
        print(f'{Fore.YELLOW}|{Style.RESET_ALL} {Fore.GREEN}1. Coloque la ruta de nombres      {Style.RESET_ALL}{Fore.YELLOW}|{Style.RESET_ALL}')
        print(f'{Fore.YELLOW}|{Style.RESET_ALL} {Fore.GREEN}    y ruta de combinaciones         {Style.RESET_ALL}{Fore.YELLOW}|{Style.RESET_ALL}')
        print(f'{Fore.YELLOW}|{Style.RESET_ALL} {Fore.GREEN}2. Seleccionar archivo de nombres  {Style.RESET_ALL}{Fore.YELLOW}|{Style.RESET_ALL}')
        print(f'{Fore.YELLOW}|{Style.RESET_ALL} {Fore.GREEN}    de su carpeta "Combo"           {Style.RESET_ALL}{Fore.YELLOW}|{Style.RESET_ALL}')
        print(f'{Fore.YELLOW}|{Style.RESET_ALL} {Fore.GREEN}3. Generador de nombres            {Style.RESET_ALL}{Fore.YELLOW}|{Style.RESET_ALL}')
        print(f'{Fore.YELLOW}|{Style.RESET_ALL} {Fore.GREEN}4. Generador de combos             {Style.RESET_ALL}{Fore.YELLOW}|{Style.RESET_ALL}')
        print(f'{Fore.YELLOW}|{Style.RESET_ALL} {Fore.GREEN}5. Multifunción para combos        {Style.RESET_ALL}{Fore.YELLOW}|{Style.RESET_ALL}')
        print(f'{Fore.YELLOW}|{Style.RESET_ALL} {Fore.GREEN}6. Generador de correos            {Style.RESET_ALL}{Fore.YELLOW}|{Style.RESET_ALL}')
        print(f'{Fore.YELLOW}|{Style.RESET_ALL} {Fore.GREEN}7. Mega Generador Mac              {Style.RESET_ALL}{Fore.YELLOW}|{Style.RESET_ALL}')
        print(f'{Fore.YELLOW}+------------------------------------+{Style.RESET_ALL}')
        opcion = input(f'\n{Fore.GREEN}🔢 Ingresa el número de opción:{Style.RESET_ALL} ')

        try:
            opcion = int(opcion)
        except ValueError:
            print(f'{Fore.RED}❌ Opción inválida. Intenta de nuevo.{Style.RESET_ALL}')
            continue

        if opcion == 1:
            nombres_archivo = input(f'\n{Fore.YELLOW}📁 Ingresa tu ruta del archivo de nombres: {Style.RESET_ALL}')
            combos_archivo = input(f'\n{Fore.YELLOW}📁 Ingresa la ruta del archivo de combinaciones: {Style.RESET_ALL}')
            if not os.path.exists(nombres_archivo) or not os.path.exists(combos_archivo):
                print(f'{Fore.RED}❌ Uno o ambos archivos no existen{Style.RESET_ALL}')
                continue
            resultados, num_combinaciones, num_omitidas = generar_combinaciones(nombres_archivo, combos_archivo)
            if not resultados:
                print(f'{Fore.RED}❌ No se generaron resultados{Style.RESET_ALL}')
                continue
            nombre_archivo = input(f'\n{Fore.YELLOW}📝 Ingresa el nombre del archivo para guardar los resultados:{Style.RESET_ALL} ')
            print(f"\n{Fore.CYAN}🔄 Procesando archivo...{Style.RESET_ALL}")
            progress_bar(5)
            now = datetime.datetime.now()
            fecha_hora_actual = now.strftime('%Y-%m-%d %H:%M:%S')
            archivo_resultados = os.path.join('/storage/emulated/0/Resultados_combinaciones', f'{nombre_archivo}.txt')
            
            with open(archivo_resultados, 'w', encoding='utf-8') as f:
                for linea in resultados:
                    f.write(linea + '\n')
            
            print(f'\n{Fore.YELLOW}+------------------------------------+{Style.RESET_ALL}')
            print(f'{Fore.GREEN}✅ Los resultados se han guardado en: {archivo_resultados}{Style.RESET_ALL}')
            print(f'{Fore.GREEN}🔢 Número de combinaciones: {num_combinaciones}{Style.RESET_ALL}')
            print(f'{Fore.YELLOW}⚠️ Combinaciones omitidas: {num_omitidas}{Style.RESET_ALL}')
            print(f'{Fore.CYAN}📅 Fecha y hora: {fecha_hora_actual}{Style.RESET_ALL}')
            
        elif opcion == 2:
            carpeta_combos_user = '/storage/emulated/0/Combo'
            archivos_combos = [f for f in os.listdir(carpeta_combos_user) if f.endswith('.txt')]
            if not archivos_combos:
                print(f'{Fore.RED}❌ No hay archivos .txt en la carpeta Combo{Style.RESET_ALL}')
                continue
            print(' ')
            print(f'{Fore.YELLOW}📁 Archivos en la carpeta{Style.RESET_ALL} "Combo":  ')
            print(' ')
            for i, archivo in enumerate(archivos_combos, 1):
                print(f' {Fore.GREEN}{i}. {archivo}{Style.RESET_ALL}  ')
            print(' ')
            seleccion_nombres = int(input(f'{Fore.GREEN}🔢 Selecciona el archivo de nombres (1-{len(archivos_combos)}): {Style.RESET_ALL}')) - 1
            seleccion_combos = int(input(f'\n{Fore.GREEN}🔢 Selecciona el archivo de combinaciones (1-{len(archivos_combos)}): {Style.RESET_ALL}')) - 1
            
            if seleccion_nombres >= len(archivos_combos) or seleccion_combos >= len(archivos_combos):
                print(f'{Fore.RED}❌ Selección inválida{Style.RESET_ALL}')
                continue
                
            nombres_archivo = os.path.join(carpeta_combos_user, archivos_combos[seleccion_nombres])
            combos_archivo = os.path.join(carpeta_combos_user, archivos_combos[seleccion_combos])
            resultados, num_combinaciones, num_omitidas = generar_combinaciones(nombres_archivo, combos_archivo)
            if not resultados:
                print(f'{Fore.RED}❌ No se generaron resultados{Style.RESET_ALL}')
                continue
            nombre_archivo = input(f'\n{Fore.YELLOW}📝 Ingresa el nombre del archivo para guardar los resultados:{Style.RESET_ALL} ')
            print(f"\n{Fore.CYAN}🔄 Procesando archivo...{Style.RESET_ALL}")
            progress_bar(5)
            now = datetime.datetime.now()
            fecha_hora_actual = now.strftime('%Y-%m-%d %H:%M:%S')
            archivo_resultados = os.path.join('/storage/emulated/0/Resultados_combinaciones', f'{nombre_archivo}.txt')
            
            with open(archivo_resultados, 'w', encoding='utf-8') as f:
                for linea in resultados:
                    f.write(linea + '\n')
            
            print(f'\n{Fore.YELLOW}+------------------------------------+{Style.RESET_ALL}')
            print(f'{Fore.GREEN}✅ Los resultados se han guardado en: {archivo_resultados}{Style.RESET_ALL}')
            print(f'{Fore.GREEN}🔢 Número de combinaciones: {num_combinaciones}{Style.RESET_ALL}')
            print(f'{Fore.YELLOW}⚠️ Combinaciones omitidas: {num_omitidas}{Style.RESET_ALL}')
            print(f'{Fore.CYAN}📅 Fecha y hora: {fecha_hora_actual}{Style.RESET_ALL}')
            
        elif opcion == 3:
            generador_nombres()
            respuesta = input(f'\n{Fore.YELLOW}❓ ¿Desea continuar en el menú principal? (s/n):{Style.RESET_ALL} ')
            if respuesta.lower() == 'n':
                break
            
        elif opcion == 4:
            generador_combos()
            respuesta = input(f'\n{Fore.YELLOW}❓ ¿Desea continuar en el menú principal? (s/n):{Style.RESET_ALL} ')
            if respuesta.lower() == 'n':
                break
            
        elif opcion == 5:
            multifuncion_combos()
            respuesta = input(f'\n{Fore.YELLOW}❓ ¿Desea continuar en el menú principal? (s/n):{Style.RESET_ALL} ')
            if respuesta.lower() == 'n':
                break
            
        elif opcion == 6:
            generador_correos()
            respuesta = input(f'\n{Fore.YELLOW}❓ ¿Desea continuar en el menú principal? (s/n):{Style.RESET_ALL} ')
            if respuesta.lower() == 'n':
                break
            
        elif opcion == 7:
            prefijos_mac = (
                'D4:CF:F9:', 'D5:CB:B3:', 'D3:FC:F9:', 'D9:CC:BF:', 'A0:BB:3E:', 
                'E7:CF:F9:', 'E3:DF:D2:', 'D8:A1:A9:', 'E9:FE:F6:', '55:93:EA:', 
                '55:92:F9:', '70:CF:B9:', '04:D6:AA:', '11:33:01:', '00:1C:19:', 
                '1A:00:6A:', '1A:00:FB:', '00:A1:79:', '00:1B:79:', '00:2A:79:', 
                '00:1A:79:', '33:44:CF:', '10:27:BE:', '00:1D:E0:', '10:2F:6B:', 
                '00:04:4B:', '74:E5:F9:', '48:B0:2D:', '00:0A:95:', '00:26:5A:', 
                '00:50:E4:', '04:A0:DE:', '12:E0:4D:', '01:E0:32:', '00:12:F0:', 
                '40:1A:2A:', '02:1D:BA:', '00:B4:8D:', '70:A6:8C:', '00:E0:8A:', 
                '17:1A:90:', '90:C8:6D:', '00:D3:7C:', '18:F9:5D:', '30:F9:5D:', 
                '18:F7:6D:', '90:F9:8D:', 'A0:01:2E:', 'A3:02:5E:', 'A8:B4:9E:', 
                'C0:BB:3E:', '00:2A:01:', '00:2A:04:', '00:2A:05:', '00:2B:06:', 
                '10:2C:01:', '03:2A:09:', '00:2A:80:', '00:1A:81:', '19:1C:79:', 
                '03:1A:39:', '00:1D:79:', '00:1E:90:', '14:6E:49:', 'B4:1C:12:', 
                '06:1C:13:', '9D:1A:14:', '08:7A:56:', '00:9C:17:', '03:8F:19:', 
                '06:7F:90:', '02:7C:17:', '19:4C:18:', '06:3D:80:', 'A4:2B:8C:', 
                'B0:4E:26:', 'C8:3D:F2:', 'F0:9E:4A:', '88:5A:92:', '2C:54:CF:', 
                '3C:22:FB:', '5C:F3:FC:', '6C:5E:7A:', '7C:9E:BD:', '8C:FA:BA:', 
                '9C:1D:58:', 'AC:3F:A4:', 'BC:6A:29:', 'CC:2D:83:', 'DC:4F:22:', 
                'EC:1F:72:', 'FC:3D:93:', '0C:5B:8F:', '1C:6F:65:', '20:4A:7B:', 
                '24:5B:8C:', '28:6C:9D:', '2C:7D:AE:', '30:8E:BF:', '34:9F:C0:', 
                '38:A0:D1:', '3C:B1:E2:', '40:C2:F3:', '44:D3:04:', '48:E4:15:', 
                '4C:F5:26:', '50:06:37:', '54:17:48:', '58:28:59:', '5C:39:6A:', 
                '60:4A:7B:', '64:5B:8C:', '68:6C:9D:', '6C:7D:AE:', '70:8E:BF:', 
                '74:9F:C0:', '78:A0:D1:', '7C:B1:E2:', '80:C2:F3:', '84:D3:04:', 
                '88:E4:15:', '8C:F5:26:', '90:06:37:', '94:17:48:', '98:28:59:', 
                '9C:39:6A:', 'A0:4A:7B:', 'A4:5B:8C:', 'A8:6C:9D:', 'AC:7D:AE:', 
                'B0:8E:BF:', 'B4:9F:C0:', 'B8:A0:D1:', 'BC:B1:E2:', 'C0:C2:F3:', 
                'C4:D3:04:', 'C8:E4:15:', 'CC:F5:26:', 'D0:06:37:', 'D4:17:48:', 
                'D8:28:59:', 'DC:39:6A:', 'E0:4A:7B:', 'E4:5B:8C:', 'E8:6C:9D:', 
                'EC:7D:AE:', 'F0:8E:BF:', 'F4:9F:C0:', 'F8:A0:D1:', 'FC:B1:E2:'
            )
            print(f"{Fore.MAGENTA}")
            print('═' * 50)
            print(f"         🌟 {Fore.YELLOW}GENERADOR MEGA COMBOS 🌟 {Fore.MAGENTA}")
            print(f"         🚀 {Fore.GREEN}QPYTHON - COMBINACIONES MAC 🚀 {Fore.MAGENTA}")
            print('═' * 50)
            print(f"{Style.RESET_ALL}")

            print(f"\n{Fore.CYAN}📋 TIPOS DE DIRECCIONES MAC DISPONIBLES:{Style.RESET_ALL}\n")
            total_prefijos = len(prefijos_mac)
            for i in range(total_prefijos):
                print(f"{Fore.GREEN}{i+1} - {prefijos_mac[i]}{Style.RESET_ALL}")

            opcion_mac = input(f"""
{Fore.CYAN}🔧 ¿QUÉ TIPO DE MAC DESEA USAR?
{Fore.GREEN}[T] Todos los tipos {Fore.RED}o {Fore.CYAN}[E] Específico{Style.RESET_ALL}
{Fore.YELLOW}🔢 Seleccione (T/E): {Style.RESET_ALL}""").upper()

            if opcion_mac.startswith('E'):
                print(f"\n{Fore.CYAN}📋 TIPOS DE MAC DISPONIBLES:{Style.RESET_ALL}\n")
                for i in range(total_prefijos):
                    print(f"{Fore.GREEN}{i+1} - {prefijos_mac[i]}{Style.RESET_ALL}")
                tipo_seleccionado = input(f"{Fore.RED}🔢 Escoja un tipo de MAC: {Style.RESET_ALL}")
            else:
                tipo_seleccionado = None

            nombre_archivo = input(f"""
{Fore.RED}📝 INGRESE EL NOMBRE PARA SU COMBO:
{Fore.YELLOW}📝 Nombre del combo: {Style.RESET_ALL}""")

            cantidad = input(f"""
{Fore.CYAN}🔢 ¿CUÁNTAS DIRECCIONES MAC DESEA CREAR?
{Fore.YELLOW}🔢 Cantidad: {Style.RESET_ALL}""")

            try:
                cantidad = int(cantidad)
                if cantidad <= 0:
                    raise ValueError("La cantidad debe ser mayor que 0.")
            except ValueError:
                print(f"{Fore.RED}❌ Error: Ingrese un número válido y mayor que 0.{Style.RESET_ALL}")
                continue

            ruta_archivo = f"/storage/emulated/0/Combo/{nombre_archivo}_Mac_Katya.txt"

            def guardar_direccion(direccion):
                with open(ruta_archivo, 'a+') as archivo:
                    archivo.write(direccion + "\n")

            print(f"\n{Fore.GREEN}🔄 GENERANDO DIRECCIONES MAC...{Style.RESET_ALL}")
            contador = 0
            while contador < cantidad:
                direccion_aleatoria = "%02x:%02x:%02x" % (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                direccion_aleatoria = direccion_aleatoria.replace('100', '10')
                
                if opcion_mac.startswith('E'):
                    try:
                        direccion = prefijos_mac[int(tipo_seleccionado)-1] + direccion_aleatoria
                    except (IndexError, ValueError):
                        print(f"{Fore.RED}❌ Error: Tipo de MAC inválido.{Style.RESET_ALL}")
                        break
                else:
                    direccion = random.choice(prefijos_mac) + direccion_aleatoria
                
                print(f"{Fore.MAGENTA}🔍 {direccion}  {Fore.YELLOW}[{contador+1}/{cantidad}]{Style.RESET_ALL}")
                guardar_direccion(direccion)
                contador += 1
                time.sleep(0.05)  

            print(f"""
{Fore.GREEN}✅ OPERACIÓN COMPLETADA
📂 Combo guardado en: {ruta_archivo}
🙌 ¡Gracias por usar el Mega Generador KATYA! 😎{Style.RESET_ALL}
""")
            respuesta = input(f'\n{Fore.YELLOW}❓ ¿Desea continuar en el menú principal? (s/n):{Style.RESET_ALL} ')
            if respuesta.lower() == 'n':
                break
            
        else:
            print(f'{Fore.RED}❌ Opción inválida. Intenta de nuevo.{Style.RESET_ALL}')

if __name__ == '__main__':
    menu_principal()