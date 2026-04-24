// Declaración de las variables
const inputNom = document.getElementById("nombre");
const inputApe = document.getElementById("apellido");
const inputEmail = document.getElementById("email");
const inputTel = document.getElementById("telefono");
const selCategoria = document.getElementById("categoria");
const inputSi = document.getElementById("cliente-si");
const inputNo = document.getElementById("cliente-no");
const tAreaComent = document.getElementById("comentario");
const btnEnviar = document.getElementById("enviar");
const btnReset = document.getElementById("reset");
const errorMens = document.getElementById("mensaje-error");
const formContacto = document.querySelector("#form-contacto");
//Una expresión regular (regex) es una forma de describir patrones de texto.
const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
/* metodo que limpia todos los campos de entradas**/
const limpiarDatos = () => {
  inputNom.value = "";
  inputApe.value = "";
  inputEmail.value = "";
  inputTel.value = "";
  selCategoria.value = "";
  inputSi.checked = false;
  inputNo.checked = false;
  tAreaComent.value = "";
  errorMens.textContent = "";
};
//Se presiona el botón borra  de los datos de input del formulario
btnReset.addEventListener("click", () => {
  limpiarDatos();
});
// Evento que hace click , previamente valida que ningun campo este vacio
formContacto.addEventListener("submit", (e) => {
  e.preventDefault();

  //Validacion de los campos vacios

  if (
    inputNom.value.trim() === "" ||
    inputApe.value.trim() === "" ||
    inputEmail.value.trim() === "" ||
    inputTel.value.trim() === "" ||
    selCategoria.value === "" ||
    tAreaComent.value.trim() === "" ||
    (!inputSi.checked && !inputNo.checked)
  ) {
    errorMens.textContent = "Campos Vacios";

    return false;
  }
  //validacion del formato
  if (!regex.test(inputEmail.value)) {
    errorMens.textContent = "El formato no es valido, debe usar @";
    return false;
  } else {
    alert("El formulario fue enviado");
    limpiarDatos();
  }
});
