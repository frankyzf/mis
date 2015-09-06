var volumeApp = angular.module('volumeApp', ['ngResource', 'ngTable']);




volumeApp.controller('servctrl', ['$scope', '$resource', '$http', '$filter', 'ngTableParams',
  function($scope, $resource, $http, $filter, ngTableParams) {
	$scope.checked = {};
    $scope.servers = $resource('/volume/server').query(function(){
        for (var serv in $scope.servers){
            $scope.checked[serv.name] = false;
        }
    });

    var getLastMonth = function(){
        var d = new Date();
        d.setMonth(d.getMonth()-1);
        return d;
    };

    $scope.fetchdate = getLastMonth();
    $scope.lastmonth = getLastMonth().getFullYear() + "-" + getLastMonth().getMonth();
    //$scope.data = [{server: "FAKE", date: new Date(), time: new Date(), side: 'Buy', symbol:'EUR/USD', bank:'BNP1', size: 100000, price: 1.3, termsize:13000} ];
    $scope.data = [];

	$scope.fetchVolume = function(){
	    var selectedservers = []
	    angular.forEach($scope.checked, function(value,key){
	        if(value == true){
	            selectedservers.push(key);
	        }
	    })
        console.log(selectedservers.toString());
	    if(selectedservers.length > 0){
            $scope.data = $resource('/volume/volume/',
                        {type: 'bymonth', servlist:selectedservers.toString(),
                        date:$scope.fetchdate.toISOString().slice(0,10).replace(/-/g,"") })
                   .query(function(){
                $scope.tableParams.reload();
            });
            console.log($scope.data)
        }
        else{
        alert("please select a server first");
        }
	};

	//ngtable
    $scope.tableParams = new ngTableParams({
        page: 1,            // show first page
        count: 10          // count per page
    }, {
        groupBy: 'server',
        total: $scope.data.length,
        getData: function($defer, params) {
            var orderedData = params.sorting() ?
                    $filter('orderBy')($scope.data, $scope.tableParams.orderBy()) :$scope.data;
            $defer.resolve(orderedData.slice((params.page() - 1) * params.count(), params.page() * params.count()));
        }
    });

    $scope.calcSum = function(data) {
        var sum = 0;
        angular.forEach(data, function(item) {
            sum += item.size;
        });
        return sum;
    }

}]);



