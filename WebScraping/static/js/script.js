document.getElementById("icon-menu").addEventListener("click", mostrar_menu);

function mostrar_menu(){

    document.getElementById("move-content").classList.toggle('move-container-all');
    document.getElementById("show-menu").classList.toggle('show-lateral');
}








                            //Buscador de contenido


//Ejecutando funciones
//document.querySelectorAll("a[href='#search']").addEventListener("click", mostrar_buscador);
document.getElementById("btn-search").addEventListener("click", mostrar_buscador);
//document.getElementById("icon-search").addEventListener("click", mostrar_buscador);
document.getElementById("cover-ctn-search").addEventListener("click", ocultar_buscador);

//Declarando variables
bars_search =       document.getElementById("ctn-bars-search");
cover_ctn_search =  document.getElementById("cover-ctn-search");
inputSearch =       document.getElementById("inputSearch");
box_search =        document.getElementById("box-search");


//Funcion para mostrar el buscador
/*
function myFunction() {
    bars_search.style.top = "120px";
    cover_ctn_search.style.display = "block";
    inputSearch.focus();
}
*/

function mostrar_buscador(){
	alert("Hiciste click");
    bars_search.style.top = "120px";
    cover_ctn_search.style.display = "block";
    inputSearch.focus();

}

//Funcion para ocultar el buscador
function ocultar_buscador(){

    bars_search.style.top = "-10px";
    cover_ctn_search.style.display = "none";
    inputSearch.value = "";

}



