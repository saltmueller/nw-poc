'use strict';

// wrap everything into an IIFE
(function() {

    var app = angular.module('exampleapp', []);

    app.controller('MyController', ['$scope', '$interval', function($scope, $interval) {
            $scope.value = 'Hello World';
            $scope.counter = 0;

            
            $interval(function () { 
                          $scope.counter++;
                      }, 1000);

        }]);

})();
