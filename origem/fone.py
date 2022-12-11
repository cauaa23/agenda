de  src . identificador  de importação  Identificador


 fone de classe :

    def  __init__ ( self , identificador : Identificador , numero : str ):
        auto . identificador  =  identificador
        auto . numero  =  numero

    @ método estático
    def  validarNumero ( numero ) ->  bool :
        válido  = [ '1' , '2' , '3' , '4' , '5' , '6 ' , '7' , '8' , '9' , '0' , '(' , ')' , '-' , '.' ]
        para  n  em  numero :
            se  n  for  válido :
                passar
            senão :
                retornar  falso
        retornar  Verdadeiro

    def  getIdentificador ( self ) ->  Identificador :
        retorne  a si mesmo . identificador

    def  getNumero ( self ) ->  str :
        retorne  a si mesmo . numero
