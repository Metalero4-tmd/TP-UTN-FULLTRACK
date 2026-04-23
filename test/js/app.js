const inputNom = document.getElementById("nombre");
const inputApe = document.getElementById("apellido");
const inputEmail = document.getElementById("email");
const inputTel = document.getElementById("telefono");
const SelCategoria = document.getElementById("categoria");
const inputSi = document.getElementById("cliente-si");
const imputNo = document.getElementById("cliente-no");
const tAreaComent = document.getElementById("comentario");
const btnEnviar = document.getElementById("enviar");
const btnReset = document.getElementById("reset");
const errorMens = document.getElementById("mensaje-error");
const formContacto = document.querySelector("#form-contacto");
const removeDate = () => {
  inputNom.value = "";
  inputApe.value = "";
  inputEmail.value = "";
  inputTel.value = "";
  SelCategoria.value = "";
  inputSi.checked = false;
  imputNo.checked = false;
  tAreaComent.value = "";
  errorMens.textContent = "";
};
//Borrado de los datos del formulario
btnReset.addEventListener("click", () => {
  removeDate();
});

formContacto.addEventListener("submit", (e) => {
  e.preventDefault();
  if (
    inputNom.value.trim() === "" ||
    inputApe.value.trim() === "" ||
    inputEmail.value.trim() === "" ||
    inputTel.value.trim() === "" ||
    SelCategoria.value === "" ||
    tAreaComent.value.trim() === "" ||
    (!inputSi.checked && !imputNo.checked)
  ) {
    errorMens.textContent = "Campos Vacios";
  } else {
    alert("El formulario fue enviado");
    removeDate();
  }
});
