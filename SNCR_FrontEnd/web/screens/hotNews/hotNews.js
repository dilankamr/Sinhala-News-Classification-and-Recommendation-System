SNCR_app.controller("hotNews", function ($scope, $controller, $http, $filter) {



    angular.extend(this, $controller('commonController', {
        $scope: $scope
    }));

    $scope.getNews('hotNews');
    console.log('hotnews get called');




});