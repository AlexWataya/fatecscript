var app = angular.module("kideliciaApp",[]);
    app.config(function($interpolateProvider){
        $interpolateProvider.startSymbol('{_');
        $interpolateProvider.endSymbol('_}');
    });

function controller($scope , $http){

    $scope.cardapios = []
    $http.get('/cardapio/crud/listar').success(function(json){
        $scope.cardapios = json;
    })

    $scope.editarLanche = function(cardapio) {
        cardapio.editando = true;
    }

    $scope.confirmarEdicao = function(cardapio) {

        cardapio.editando = false;

        params = {"idCardapio": cardapio.id,
                    "lanche": cardapio.lanche,
                    "ingrediente": cardapio.ingrediente,
                    "valor": cardapio.valor
        }

        $http.post('/cardapio/crud/editar_lanche', params)

    }

    $scope.removerElemento = function(cardapio, index) {
        $scope.cardapios.splice(index, 1)
        cardapio.editando = false;

        $http.post('/cardapio/crud/remover_lanche', {"idCardapio": cardapio.id})
    }
}