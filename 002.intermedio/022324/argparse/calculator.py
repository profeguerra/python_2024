import argparse

parse = argparse.ArgumentParser(description='Es una calculadora que te permite sumar, restar y multiplicar dos numeros')
parse.add_argument('-num_uno', '--numero_uno', type=int, help='Parametro uno')
parse.add_argument('-num_dos', '--numero_dos', type=int, help='Parametro dos')
parse.add_argument(
    '-operation', '--operation',
    type=str,
    choices=['suma', 'resta', 'multiplicacion'],
    default='suma', 
    required=False,
    help='Operacion seleccionada para los numeros ingresados'
    )


args = parse.parse_args()

if args.operation == 'suma':
    print(args.numero_uno + args.numero_dos)
elif args.operation == 'resta':
    print(args.numero_uno - args.numero_dos)
elif args.operation == 'multiplicacion':
    print(args.numero_uno * args.numero_dos)
