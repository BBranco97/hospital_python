import os

class medico:
    crm=""
    nome=""
    nascimento=""
    especialidade=""
    universidade=""
    email=""
    telefone=""

class paciente:
    cpf=""
    nome=""
    nascimento=""
    sexo=""
    plano=""
    email=""
    telefone=""

class consulta:
    crm=""  
    cpf=""
    data=""
    hora=""
    diagnostico=""
    medicamentos=[]

def le_arquivo_medicos(arq_medicos):
    medicos = []
    if os.path.exists(arq_medicos):
        arquivo = open(arq_medicos, 'r')
        for linha in arquivo:
            infos_medico = linha.strip().split(';')
            m = medico()
            m.crm= infos_medico[0]
            m.nome= infos_medico[1]
            m.nascimento= infos_medico[2]
            m.especialidade=infos_medico[3]
            m.universidade=infos_medico[4]
            m.email=infos_medico[5]
            m.telefone=infos_medico[6]
            medicos.append(m)
        arquivo.close()
    return medicos

def le_arquivo_pacientes(arq_pacientes):
    pacientes = []
    if os.path.exists(arq_pacientes):
        arquivo = open(arq_pacientes, 'r')
        for linha in arquivo:
            infos_paciente = linha.strip().split(';')
            p = paciente()
            p.cpf=infos_paciente[0]
            p.nome=infos_paciente[1]
            p.nascimento=infos_paciente[2]
            p.sexo=infos_paciente[3]
            p.plano=infos_paciente[4]
            p.email=infos_paciente[5]
            p.telefone=infos_paciente[6]
            pacientes.append(p)
        arquivo.close()
    return pacientes

def le_arquivo_consultas(arq_consultas):
    consultas = []
    if os.path.exists(arq_consultas):
        arquivo = open(arq_consultas, 'r')
        for linha in arquivo:
            infos_consulta = linha.strip().split(';')
            c = consulta()
            c.crm=infos_consulta[0]  
            c.cpf=infos_consulta[1]
            c.data=infos_consulta[2] 
            c.hora=infos_consulta[3]
            c.diagnostico=infos_consulta[4]
            remedios=infos_consulta[5]
            c.medicamentos=remedios.strip().split(", ") 
            consultas.append(c)
        arquivo.close()
    return consultas

def salva_arquivo_medicos(medicos,arq_medicos):
    arquivo = open(arq_medicos, "w")
    for m in medicos:
        arquivo.write(m.crm + ';' + m.nome + ';' + m.nascimento + ';' + m.especialidade + ';' + m.universidade + ';' + m.email + ';' + m.telefone + '\n')
    arquivo.close()

def salva_arquivo_pacientes(pacientes,arq_pacientes):
    arquivo = open(arq_pacientes, "w")
    for p in pacientes:
        arquivo.write(p.cpf + ";" + p.nome + ";" + p.nascimento + ";" + p.sexo + ";" + p.plano + ";" + p.email + ";" + p.telefone + '\n')
    arquivo.close()

def salva_arquivo_consultas(consultas,arq_consultas):
    arquivo = open(arq_consultas, "w")
    for c in consultas:
        remedios=" ".join(c.medicamentos)
        retirar="[]'"
        for i in range(len(retirar)):
            remedios=remedios.replace(retirar[i],"")
        arquivo.write(c.crm + ";" + c.cpf + ";" + c.data + ";" + c.hora + ";" + c.diagnostico + ";" + remedios +'\n')
    arquivo.close()  

def imprime_medico(m):
    print("---------------------------")
    print(f"{m.crm} | {m.nome} | {m.nascimento} | {m.especialidade} | {m.universidade} | {m.email} | {m.telefone}")
    print("---------------------------")

def imprime_paciente(p):
    print("---------------------------")
    print(f"{p.cpf} | {p.nome} | {p.nascimento} | {p.sexo} | {p.plano} | {p.email} | {p.telefone}")
    print("---------------------------")

def imprime_consulta(c):
    print("---------------------------")
    remedios=" ".join(c.medicamentos)
    retirar="[]'"
    for i in range(len(retirar)):
        remedios=remedios.replace(retirar[i],"")
  
    print(f"{c.crm} | {c.cpf} | {c.data} | {c.hora} | {c.diagnostico} | {remedios}")
    print("---------------------------")

def listar_todos_medicos(medicos):
    if(len(medicos)==0):
        print("Não ha dados")
    for i in range (len(medicos)):
        m=medicos[i]
        imprime_medico(m)

def listar_todos_pacientes(pacientes):
    if(len(pacientes)==0):
        print("Não ha dados")
    for i in range (len(pacientes)):
        p=pacientes[i]
        imprime_paciente(p)

def listar_todas_consultas(consultas):
    if(len(consultas)==0):
        print("Não ha dados")
    for i in range (len(consultas)):
        c=consultas[i]
        imprime_consulta(c)

def buscar_medico(medicos):
    crm=input("Digite o CRM para consulta: ")
    for i in range (len(medicos)):
        m=medicos[i]
        if m.crm==crm:
            return i
    return -1

def buscar_paciente(pacientes):
    cpf=input("Digite o CPF para consulta: ")
    for i in range (len(pacientes)):
        p=pacientes[i]
        if p.cpf==cpf:
            return i
    return -1

def buscar_consulta(consultas):
    print("Digite os dados para a consulta: ")
    crm=input("Digite o CRM: ")
    cpf=input("Digite o CPF: ")
    data=input("Digite a data no formato dd/mm/aaaa: ") 
    hora=input("Digite a hora: ")
    for i in range(len(consultas)):
        c=consultas[i]
        if c.crm==crm and c.cpf==cpf and c.data==data and c.hora==hora:
            return i
    return -1

def listar_um_medico(medicos):
    i=buscar_medico(medicos)
    if i==-1:
        print("CRM não cadastrado")
    else:
        imprime_medico(medicos[i])

def listar_um_paciente(pacientes):
    i=buscar_paciente(pacientes)
    if i==-1:
        print("CPF não cadastrado")
    else:
        imprime_paciente(pacientes[i])

def listar_uma_consulta(consultas):
    i=buscar_consulta(consultas)
    if i==-1:
        print("Dados não encontrados")
    else:
        imprime_consulta(consultas[i])

def criar_medico(medicos):
    m=medico()
    m.crm=input("Informe o CRM: ")
    m.nome=input("Informe o nome: ")
    m.nascimento=input("Informe a data de nascimento: ")
    m.especialidade=input("Informe a especialidade: ")
    m.universidade=input("Informe a universidade: ")
    m.email=input("Informe o email: ")
    m.telefone=input("Informe o telefone: ")
    medicos.append(m)

def criar_paciente(pacientes):
    p=paciente()
    p.cpf=input("Informe o CPF: ")
    p.nome=input("Informe o nome: ")
    p.nascimento=input("Informe a data de nascimento: ")
    p.sexo=input("Informe o sexo: ")
    p.plano=input("Informe o plano de saúde: ")
    p.email=input("Informe o email: ")
    p.telefone=input("Informe o telefone: ")
    pacientes.append(p)

def criar_consulta(consultas):
    c=consulta()
    c.crm=input("Informe o CRM: ")  
    c.cpf=input("Informe o CPF: ")
    c.data=input("Informe a data no formato dd/mm/aaa: ")
    c.hora=input("Infome a hora: ")
    c.diagnostico=input("Informe o diagnóstico: ")
    remedios=input("Digite o(s) medicamento(s) no formato A, B, C...: ")
    c.medicamentos=remedios.split(", ")
    consultas.append(c)

def incluir_medico(medicos):
    i= buscar_medico(medicos)
    if i==-1:
        print("CRM não encontrado, siga os passos para o cadastro")
        criar_medico(medicos)
        print("Médico adicionado com sucesso")
    else:
        print("Médico já cadastrado")

def incluir_paciente(pacientes):
    i= buscar_paciente(pacientes)
    if i==-1:
        print("CPF não encontrado, siga os passos para o cadastro")
        criar_paciente(pacientes)
        print("Paciente adicionado com sucesso")
    else:
        print("Paciente já cadastrado")    

def incluir_consulta(consultas):
    i= buscar_consulta(consultas)
    if i==-1:
        print("Dados não encontrados, siga os passos para o cadastro")
        criar_consulta(consultas)
        print("Consulta adicionada com sucesso")
    else:
        print("Consulta já cadastrada")

def remover(lista, i):
    lista[i] = lista[len(lista) - 1]
    lista.pop()

def excluir_medico(medicos):
    if len(medicos) == 0:
        print("Nao ha médicos cadastrados")
    else:
        i=buscar_medico(medicos)
        if i != -1:
            imprime_medico(medicos[i])
            confirmacao=input("Deseja excluir? 'S'/'N': ")
            if confirmacao == "S" or confirmacao=="s":
                remover(medicos,i)
                print("Médico removido com sucesso")
            else:
                print("Cancelado")
        else:
            print("Médico não encontrado")

def excluir_paciente(pacientes):
    if len(pacientes) == 0:
        print("Nao ha pacientes cadastrados")
    else:
        i=buscar_paciente(pacientes)
        if i != -1:
            imprime_paciente(pacientes[i])
            confirmacao=input("Deseja excluir? 'S'/'N': ")
            if confirmacao == "S" or confirmacao=="s":
                remover(pacientes,i)
                print("Paciente removido com sucesso")
            else:
                print("Cancelado")
        else:
            print("Médico não encontrado")

def excluir_consulta(consultas):
    if len(consultas) == 0:
        print("Nao ha consultas cadastradas")
    else:
        i=buscar_consulta(consultas)
        if i != -1:
            imprime_consulta(consultas[i])
            confirmacao=input("Deseja excluir? 'S'/'N': ")
            if confirmacao == "S" or confirmacao=="s":
                remover(consultas,i)
                print("Consulta removida com sucesso")
            else:
                print("Cancelado")
        else:
            print("Consulta não encontrada")

def alterar_medico (medicos):
    i=buscar_medico(medicos)
    if i!=-1:
        medicos[i].nome = input("Informe o novo nome: ")
        medicos[i].email= input("Informe o novo email: ")
        medicos[i].telefone= input("Informe o novo telefone: ")
        print("Médico atualizado com sucesso")
    else:
        print("Médico não encontrado")

def alterar_paciente (pacientes):
    i=buscar_paciente(pacientes)
    if i!=-1:
        pacientes[i].nome= input ("informe o novo nome: ")
        pacientes[i].sexo= input ("Informe o novo sexo: ")
        pacientes[i].plano= input("Informe o novo plano de saúde: ")
        pacientes[i].email= input("Informe o novo email: ")
        pacientes[i].telefone = input("Informe o novo telefone: ")
        print("Paciente atualizado com sucesso")
    else:
        print("Paciente não encontrado")       

def alterar_consulta (consultas):
    i=buscar_consulta (consultas)
    if i!=-1:
        consultas[i].diagnostico= input("informe o novo diagnóstico: ")
        remedios=input("Digite os novos medicamentos: ")
        consultas[i].medicamentos=remedios.split(", ") 
        print("Consulta atualizada com sucesso")
    else:
        print("Consulta não encontrada")  

def menu ():
    print("---------------------------")
    print("MENU")
    print("---------------------------")
    print("1- Submenu de Médicos")
    print("2- Submenu de Pacientes")
    print("3- Submenu de Consultas")
    print("4- Submenu de Relatórios")
    print("5- Sair")
    print("---------------------------")    
    op=input()
    return op

def submenu ():
    print("---------------------------")
    print("1- Listar todos")
    print("2- Listar um")
    print("3- Incluir")
    print("4- Alterar os dados")
    print("5- Excluir")
    print("6- Voltar ao menu principal")
    print("---------------------------")
    op=input()
    return op

def submenu_relatórios ():
    print("---------------------------")
    print("SUBMENU DE RELATÓRIOS")
    print("---------------------------")
    print("1- Mostrar todos os médicos de uma especialidade")
    print("2- Mostrar todos os dados dos pacientes de um plano de saúde")
    print("3- Detalhamento de consultas entre dois dias")
    print("4- Voltar ao menu")
    print("---------------------------")
    op=input()
    return op

def listar_por_especialidade(medicos):
    cont=0
    if len(medicos)==0:
        print("Não há medicos cadastrados")
    else:
        especialidade=input("Digite a especialidade: ")
        for i in range (len(medicos)):
            if medicos[i].especialidade.lower()==especialidade.lower():
                imprime_medico(medicos[i])
                cont+=1
        if(cont==0):
            print("Não há medicos dessa especialidade")

def listar_por_plano(pacientes):
    cont=0
    if len(pacientes)==0:
        print("Não há pacientes cadastrados")
    else:
        plano=input("Digite o plano de saúde: ") 
        for i in range (len(pacientes)):
            if pacientes[i].plano.lower()==plano.lower():
                imprime_paciente(pacientes[i])
                cont+=1
        if(cont==0):
            print("Não há pacientes desse plano")

def confere_ano_bissexto (ano):
    if((ano%100==0 and ano%400==0)):
        return True
    elif(ano%4==0 and ano%100!=0):
        return True
    else:
        return False

def confere_dia (dia,mes,ano):
    if((mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12) and dia<=31):
        return True
    elif((mes==2 and confere_ano_bissexto(ano)) and dia<=29):
        return True
    elif((mes==2 and not confere_ano_bissexto(ano)) and dia<=28):
        return True
    elif((mes==4 or mes==6 or mes==9 or mes==11)and dia<=30):
        return True
    else:
        return False

def confere_mes (mes):
    if mes>=1 and mes<=12:
        return True
    return False

def confere_ano(ano):
    if ano>1000:#limmitação do remonta data
        return True
    return False

def remonta_data(dia,mes,ano):#não inclui zeros a direita de anos < 1000
    if dia<10 and mes<10: 
        data=("0"+str(dia)+"/"+"0"+str(mes)+"/"+str(ano))
    elif dia<10:
        data=("0"+str(dia)+"/"+str(mes)+"/"+str(ano))
    elif mes<10:
        data=(str(dia)+"/"+"0"+str(mes)+"/"+str(ano))
    else:
        data=(str(dia)+"/"+str(mes)+"/"+str(ano))
    return data

def soma_dias(X):
    data=X.strip().split("/")
    dia=int(data[0])
    mes=int(data[1])
    ano=int(data[2])
    if confere_dia(dia+1,mes,ano):
        dia+=1
    elif confere_mes(mes+1):
        mes+=1
        dia=1
    elif confere_ano(ano):
        ano+=1
        mes=1
        dia=1
    else:
        print("Data incompatível")
    data=remonta_data(dia,mes,ano)
    return data

def confere_datas(dia_ini,mes_ini,ano_ini,dia_fim,mes_fim,ano_fim):
    if confere_dia(dia_ini,mes_ini,ano_ini) and confere_dia(dia_fim,mes_fim,ano_fim) and confere_mes(mes_ini) and confere_mes(mes_fim) and confere_ano(ano_ini) and confere_ano(ano_fim):
        if ano_fim>ano_ini:
            return True
        elif ano_fim==ano_ini and mes_fim>mes_ini:
            return True
        elif ano_fim==ano_ini and mes_fim==mes_ini and dia_fim>=dia_ini:
            return True
        else :
            return False
    else:
        return False

def listar_por_datas(consultas):
    if len(consultas)==0:
        print("Não há consultas cadastradas")
    else:
        X=input("Digite a data inicial para pesquisa no formato dd/mm/aaaa: ") 
        Y=input("Digite a data final para pesquisa no formato dd/mm/aaaa: ")
        
        data_ini=X.strip().split("/")
        dia_ini=int(data_ini[0])
        mes_ini=int(data_ini[1])
        ano_ini=int(data_ini[2])

        data_fim=Y.strip().split("/")
        dia_fim=int(data_fim[0])
        mes_fim=int(data_fim[1])
        ano_fim=int(data_fim[2])

        check=confere_datas(dia_ini,mes_ini,ano_ini,dia_fim,mes_fim,ano_fim)

        if check == False:
            print("As datas estão erradas")
        else:
            var=0
            while (check):
                for i in range (len(consultas)):
                    c=consultas[i]
                    if c.data==X: 
                        imprime_consulta(consultas[i])
                        var+=1
                X=soma_dias(X) 
                data_ini=X.strip().split("/")
                dia_ini=int(data_ini[0])
                mes_ini=int(data_ini[1])
                ano_ini=int(data_ini[2])
                check=confere_datas(dia_ini,mes_ini,ano_ini,dia_fim,mes_fim,ano_fim)
            if var==0:
                print("Não há consultas entre as datas")

def main():
    arq_medicos="arq_medicos.txt"
    arq_pacientes="arq_pacientes.txt"
    arq_consultas="arq_consultas.txt"

    op=menu()
    while op!="#5!":
        op2=""
        if op=="1":
            while op2!="#6!":
                print("---------------------------")
                print("SUBMENU DE MÉDICOS")
                medicos= le_arquivo_medicos(arq_medicos)
                op2=submenu()
                if op2=="1":
                    listar_todos_medicos(medicos)
                elif op2=="2":
                    listar_um_medico(medicos)
                elif op2=="3":
                    incluir_medico(medicos)
                    salva_arquivo_medicos(medicos,arq_medicos)
                elif op2=="4":
                    alterar_medico(medicos)
                    salva_arquivo_medicos(medicos,arq_medicos)
                elif op2=="5":
                    excluir_medico(medicos)
                    salva_arquivo_medicos(medicos,arq_medicos)
                elif op2=="6":
                    op2="#6!"
                    op=menu()
                else:
                    print("Opção inválida") 
            
        elif op=="2":
            op2=""
            while(op2!="#6!"):
                print("---------------------------")
                print("SUBMENU DE PACIENTES")
                pacientes=le_arquivo_pacientes(arq_pacientes)
                op2=submenu()
                if op2=="1":
                    listar_todos_pacientes(pacientes)
                elif op2=="2":
                    listar_um_paciente(pacientes)
                elif op2=="3":
                    incluir_paciente(pacientes)
                    salva_arquivo_pacientes(pacientes,arq_pacientes)
                elif op2=="4":
                    alterar_paciente(pacientes)
                    salva_arquivo_pacientes(pacientes,arq_pacientes)
                elif op2=="5":
                    excluir_paciente(pacientes)
                    salva_arquivo_pacientes(pacientes,arq_pacientes)
                elif op2=="6":
                    op2="#6!"
                    op=menu()
                else: 
                    print("Opção inválida") 

        elif op=="3":
            while(op2!="#6!"):
                print("---------------------------")
                print("SUBMENU DE CONSULTAS")
                consultas= le_arquivo_consultas(arq_consultas)
                op2=submenu()
                if op2=="1":
                    listar_todas_consultas(consultas)
                elif op2=="2":
                    listar_uma_consulta(consultas)
                elif op2=="3":
                    incluir_consulta(consultas)
                    salva_arquivo_consultas(consultas,arq_consultas)
                elif op2=="4":
                    alterar_consulta(consultas)
                    salva_arquivo_consultas(consultas,arq_consultas)
                elif op2=="5":
                    excluir_consulta(consultas)
                    salva_arquivo_consultas(consultas,arq_consultas)
                elif op2=="6":
                    op2="#6!"
                    op=menu()
                else:
                    print("Opção inválida") 

        elif op=="4":
            while op2!="#4!":
                medicos= le_arquivo_medicos(arq_medicos)
                pacientes= le_arquivo_pacientes(arq_pacientes)
                consultas= le_arquivo_consultas(arq_consultas)
                op2=submenu_relatórios()
                if op2=="1":
                    listar_por_especialidade(medicos)
                elif op2=="2":
                    listar_por_plano(pacientes)
                elif op2=="3":
                    listar_por_datas(consultas)
                elif op2=="4":
                    op2="#4!"
                    op=menu()
                else:
                    print("Opção inválida") 
        
        elif op=="5":
            print("Obrigado por utilizar o programa")
            op="#5!"
        
        else:
            print("Opção inválida")
            op=menu()

main()