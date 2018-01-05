def generate(length=5):
    return ['10.10.10.{}'.format(i) for i in range(length)]

generate()
