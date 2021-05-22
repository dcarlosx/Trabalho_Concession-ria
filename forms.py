<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Formulário</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-+0n0xVW2eSR5OomGNYDnhzAbDsOXxcvSN1TPprVMTNDbiYZCxYbOOl7+AMvyTG2x" crossorigin="anonymous">
</head>

<body>
    <div class="col-8 m-auto pt-2 pb-2 text-center">
        <h1>Cadastro</h1>
    </div>

    <div class="col-8 m-auto pt-3 pb-2 text-center">
        <a href="/" class="btn btn-info">Voltar</a>
    </div>

    <div class="col-8 m-auto pt-4 pb-2 text-center">
        <form name="form"  id="form" action="/create/" method="post">
            {% csrf_token %}
            <!--{{form.as_p}}-->
            <div class="form-group mt-4">Cliente: {{form.cliente}}</div>
            <div class="form-group mt-4">Sexo: {{form.sexo}}</div>
            <div class="form-group mt-4">Endereço: {{form.endereco}}</div>
            <div class="form-group mt-4">Telefone: {{form.telefone}}</div>
            <input type="submit" class="btn btn-success" value="Salvar">
        </form>
    </div>
</body>
</html>
