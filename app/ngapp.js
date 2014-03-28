'use strict';

// wrap everything into an IIFE
(function() {

    var app = angular.module('exampleapp', []);

    app.controller('MyController', ['$scope', '$interval', 'dataService', 
        function($scope, $interval, dataService) {
            $scope.value = 'Hello World';
            $scope.counter = 0;

            $scope.entries = [];
            
            $interval(function () { 
                          $scope.counter++;
                      }, 1000);

            var MAX_ENTRIES=10;
            dataService.onMessage(function(message) {
                entries.push(message);
            });

        }]);

    // service to read the data
    app.factory('dataService', [
        function() {

            var mqtt = require('mqtt')

            var client = mqtt.createClient(1883, 'localhost');
            client.subscribe('linux/metrics');

            var callbacks = [];
            client.on('message', function (topic, message) {
                for(var i=0; i < callbacks.length; i++)
                    callbacks[i](message);
                }
            });

            return {
                onMessage: function (callbackFn) {
                    callbacks.push(callbackFn);
                }
            };

    }]);

})();
