/**
 *  AngularJS for Index.html
 */

// Declare and Configure app
var app = angular.module('searchApp', ['ngCookies']);
app.config(['$interpolateProvider', function($interpolateProvider) {
	$interpolateProvider.startSymbol('{[');
	$interpolateProvider.endSymbol(']}');
}]);

// Define functionality of app
app.controller('myCtrl', ['$scope', '$http', '$cookies', 
function($scope,$http, $cookies) {
	$scope.sendPost = function() {

	// Set cookie for search term
	$cookies.put('search_term' , $scope.search_term);

	// Fetch results for search term
	$http.post("/", {text:$scope.search_term}).then(function(response){
		$scope.stati = response.data.stati;
		$scope.error_message = response.data.error_message;
		});//end response and post

	};//end sendPost
}]);//end controller