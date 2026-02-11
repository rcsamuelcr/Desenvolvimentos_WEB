programa{
    funcao inicio (){
        inteiro numero, lim_tabu
        inteiro i = 0

        escreva("Digite o número que queira saber a tauada")
        leia(numero)

        escreva("Digite o numero que a tabuada se extenderá")
        leia(lim_tabu)

        se(numero >= 10){
            escreva("o número que você digitou é maior ou igual a 10 (dez) e, se dividido por 2 é igual a", (numero/2) ,"\n")
        }
        senao{
            escreva("O número digitado foi", numero, "\n")
        }

        enquanto(i <= lim_tabu){
            escreva(i, "X", numero, "=", i * numero, "\n")
            i++
        }

    }
}