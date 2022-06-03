function profileMap() {
    var mapProp = {
      center: new google.maps.LatLng(45.7315635, -122.6362767),
      zoom: 5,
    };
    var map = new google.maps.Map(document.getElementById("googleMap"), mapProp);
}
