import json
with open("dados.json", "r", encoding="utf-8") as arquivo:
    dados=json.load(arquivo)
def cadastro(lista):
    novo_cadastro={}
    while True:
        novo_cadastro.clear()
        print('=+='*30)
        print('MENU DE CADASTRO') 
        print('=+='*30)
        novo_cadastro['nome']=str(input('digite seu primeiro nome:')).strip().capitalize()
        novo_cadastro['sobrenome']=str(input('digite seu sobrenome:')).strip().capitalize()
        while True:
         novo_cadastro['cpf']=str(input('digite seu cpf:'))
         tru=False
         for i in dados:
            
            if i['cpf']== novo_cadastro['cpf']:
                tru=True
                print('[ERRO] cpf exintente')
                break
         if tru==False:
             break
        novo_cadastro['data_nascimento']=str(input('digite sua data de nascimento:')).strip()
        novo_cadastro['sexo']=str(input('qual o seu sexo?[masculino/feminino]:')).strip().capitalize()
        novo_cadastro['raca_cor']=str(input('qual sua raça/cor?')).strip().capitalize() 
        
        dados.append(novo_cadastro.copy())
        
        cadastro=str(input('deseja cadastrar mais ?[S/N]')).strip().upper()[0]
        while cadastro not in 'SN':
            print('[ERRO] digite uma opção válida. ')
            cadastro=str(input('deseja cadastrar mais ?[S/N]')).strip().upper()[0]
        if cadastro =='N':
                break
            


    with open("dados.json", "w", encoding="utf-8") as arquivo:
     json.dump(dados,arquivo, ensure_ascii=False, indent=2)

def pesquisa(dados):
    possiveis_resultados=list()
    while True:
        
        confere=str(input('digite uma informação para pesquisa de usuário:')).strip().capitalize()
        novos_resultados=[]
        if len(possiveis_resultados) == 0:
          for i in dados:
            for k,v in i.items():
                if confere.lower() in str(v).lower():
                    novos_resultados.append(i)
        else:
            for i in possiveis_resultados:
                for k,v in i.items():
                  if confere.lower() in str(v).lower():
                      novos_resultados.append(i)
                
        possiveis_resultados=novos_resultados.copy()
        print(f'{len(possiveis_resultados)} POSSIVEIS RESULTADOS')  
        while True:      
            confere_continua=str(input('deseja fornecer mais informações para melhor filtragem de resultados?[S/N]')).strip().upper()[0]
            while confere_continua not in 'SN':
                print('[ERRO] digite um valor valido.')
                confere_continua=str(input('deseja fornecer mais informações para melhor filtragem de resultados?[S/N]')).strip().upper()[0]
            if confere_continua == 'N':
                  break
            confere=str(input('digite uma informação para pesquisa de usuário:')).strip().capitalize()
            novos_resultados=[]
            if len(possiveis_resultados) == 0:
                for i in dados:
                    for k,v in i.items():
                        if confere.lower() in str(v).lower():
                            novos_resultados.append(i)
            else:
                    for i in possiveis_resultados:
                        for k,v in i.items():
                          if confere.lower() in str(v).lower():
                              novos_resultados.append(i)       
            possiveis_resultados=novos_resultados.copy()
            print(f'{len(possiveis_resultados)} POSSIVEIS RESULTADOS')  
        print(f'{possiveis_resultados}')        
        escolha_pesquisa=str(input('deseja pesquisar outro cadastro?[S/N]:')).strip().upper()[0]  
        while escolha_pesquisa not in 'SN':
             print('[ERRO] digite uma opção valida.')
             escolha_pesquisa=str(input('deseja pesquisar outro cadastro?[S/N]:')).strip().upper()[0]  
        if escolha_pesquisa == 'N':
             break
         
         
def conferencia(dados):
    cpfs=[]
    duplicados=[]
    for i in dados:
        if i['cpf'] in cpfs:
            print(f"cpf duplicado {i['cpf']} ") 
            duplicados.append(i['cpf'])
        else:
           cpfs.append(i['cpf'])
    print(f"{len(duplicados)} cpfs duplicados")
    print(duplicados)
     
    print('fim da conferencia.')   
    
    
    
def excluir(dados):
    possivei_usuarios=[]
    print('=+='*30)
    print('MENU DE EXCLUSÃO')
    print('=+='*30) 
    while True:
        novos_possiveis_usuarios=[]
        opcao=str(input('digite dados sobre o usuário que procura:')).strip().capitalize()
        if len(possivei_usuarios) == 0:
           for i in dados:
               for k,v in i.items():
                   if opcao.lower() in str(v).lower():
                       novos_possiveis_usuarios.append(i)
        else:
            for i in possivei_usuarios:
                for k,v in i.items():
                    if opcao.lower() in str(v).lower():
                        novos_possiveis_usuarios.append(i)
        possivei_usuarios =novos_possiveis_usuarios.copy()
        print(f'{len(possivei_usuarios)} POSSIVEIS RESULTADOS')
        
        while True:
            mais_informacao=str(input('deseja fornecer mais informações para filtrar melhor os resultados? [S/N]')).strip().upper()[0]
            while mais_informacao not in 'SN':
                print('ERRO digite uma opção valida !')
                mais_informacao=str(input('deseja fornecer mais informações para filtrar melhor os resultados? [S/N]')).strip().upper()[0]
            if mais_informacao == 'N':
                break
            novos_possiveis_usuarios=[]
            opcao=str(input('digite dados sobre o usuário que procura:')).strip().capitalize()
            if len(possivei_usuarios) == 0:
                for i in dados:
                    for k,v in i.items():
                        if opcao.lower() in str(v).lower():
                             novos_possiveis_usuarios.append(i)
            else:
                for i in possivei_usuarios:
                    for k,v in i.items():
                        if opcao.lower() in str(v).lower():
                            novos_possiveis_usuarios.append(i)
        possivei_usuarios =novos_possiveis_usuarios.copy()
        print(f'{len(possivei_usuarios)} POSSIVEIS RESULTADOS')
        for n,r in enumerate(possivei_usuarios,1):
            print(f'{n}:{r}')
        escolha_excluir=int(input('digite o numero do cadastro que deseja excluir:'))
        while escolha_excluir < 1 or escolha_excluir >  len(possivei_usuarios):
            print('[ERRO] digite uma escolha valida !')
            escolha_excluir=int(input('digite o numero do cadastro que deseja excluir:'))
        indice=escolha_excluir-1
        print(f'CADASTRO QUE SERA EXCLUIDO\n{possivei_usuarios[indice]} ')
        confirmaçao=str(input('tem certeze que deseja excluir esse cadastro?[S/N]')).strip().upper()[0]
        while confirmaçao not in 'SN':
            print(['[ERRO] digite uma opção valida !'])
            confirmaçao=str(input('tem certeze que deseja excluir esse cadastro?[S/N]')).strip().upper()[0]
        if confirmaçao == 'N':
          break
        else:
         for i in dados:
             if i == possivei_usuarios[indice]:
               print(f'antes {dados}')
               dados.remove(i) 
               print(f'depois {dados}')
               break
               
        break
    with open("dados.json", "w", encoding="utf-8") as arquivo:
     json.dump(dados,arquivo, ensure_ascii=False,indent=2)  
    
      
def menu(dados):
    while True:
      print('=+='*30)
      print('MENU DO USUÁRIO')
      print('=+='*30)
      print('1: cadastro\n2:pesquisa de cadastros\n3:conferir\n4:excluir\n5:sair.')
      print('=+='*30)
      opcao=int(input('escolha uma das opções:'))
      while opcao not in (1,2,3,4,5):
        print('[ERRO] digite uma opção valida.')
        opcao=int(input('escolha uma das opções:'))
      if opcao == 1 :
        cadastro(dados)
      elif opcao ==2:
        pesquisa(dados)
      elif opcao == 3:
        conferencia(dados) 
      elif opcao == 4:
          excluir(dados) 
      elif opcao ==5:
         break
    print('fim...')    
    
menu(dados)