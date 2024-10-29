programa {

  //banco de informações
  inteiro bag = 1, bcc = 1, bsn =123, i
  caracter voltar, deposito
  real saldo = 1000, limite = 1500, total = limite + saldo, deposito
  real credito, debito

  funcao vetor (){

    para (i=1; i<1000; i++){

      credito [i] = 0.0
    }
    para (i=1; i<1000; i++){

      debito [i] = 0.0
    }

  }

  funcao inicio(){

    inteiro ag, cc, sn
    faca{

    escreva ("\n------------- Bem Vindo ao Banco Senac -------------\n")
    escreva ("Informe o número da agência:\n")
    leia (ag)

    escreva ("informe o número da conta:\n")
    leia (cc)

    escreva ("Informe a senha:\n")
    leia (sn)
    limpa ()

    } enquanto(bag != ag   ou bcc != cc ou bsn != sn)

    menu ()

  }
  
  funcao menu() {
    inteiro op


    escreva ("Escolha uma operação abaixo\n\n")
    escreva ("1 - Saldo | 2 - Extrato | 3 - Saque | 4 - Depósito | 5 - Sair\n\n")
    escreva ("Opção:\n\n")
    leia (op)
    limpa()
    escolha (op){

    caso 1:
    saldo ()
    pare
    caso 2:
    extrato ()
    pare 
    caso 3:
    saque ()
    pare 
    caso 4:
    deposito ()
    pare
    caso 5:
    pare 

    caso contrario: escreva ("Opção Invalida, tente novamente")
    }

  }

      funcao saldo (){
        faca {

          

      escreva ("Deseja voltar ao menu principal s|n\n")
      escreva ("Saldo:", saldo, "\n")
      escreva ("Limite:", limite,"\n")
      escreva ("Total:", total,"\n")
      leia (voltar)
      }
      enquanto (voltar != "s")
      menu()

      }
      
      funcao extrato (){
        faca{

        escreva (saldo + deposito, "\n\n")
        escreva ("------------------\n\n")

        escreva ("Deseja voltar ao menu principal s|n?")
        leia (voltar)
      }
      enquanto (voltar != "s")
      menu()
      }

      funcao saque (){
        faca{

        escreva ("Deseja voltar ao menu principal s|n?")
        leia (voltar)
      }
      enquanto (voltar != "s")
      menu()
      }

      funcao deposito(){
        faca{

        escolha ("Qual valor deseja depositar: ")
        leia (deposito)
        escreva ("---------------------\n\n")

        escreva ("Deseja voltar ao menu principal s|n?")
        leia (voltar)
      }
      enquanto (voltar != "s")
      menu()
      }
}


