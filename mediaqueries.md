Mediaqueries
Son clave para el diseño de webs responsivas.
Conceptos clave
•	width -> Ancho
•	height -> alto
•	orientation: landscape -> "celular acostado"
•	Modo de pantalla -> Orientation Portrait
________________________________________
Breakpoint (puntos de interrupción)
Medidas de ancho de pantalla donde el diseño decide cambiar:
•	Teléfonos: < 600px
•	Tablets: 600px - 1024px
•	Desktop: > 1024px
________________________________________
Mobile First
La forma ideal de maquetar considerando una web responsive desde cero:
1.	Primero escribís los estilos para pantallas pequeñas (no usas mediaqueries).
2.	Luego lo ajustás a pantallas más grandes y complejas.
3.  Es mas facil pasar de mobile ->deskopt que al reves es mas complicado
trabajamos con la metodologia ->desktop firt
-simplificar


320px — 480px: Mobile devices
481px — 768px: iPads, Tablets
769px — 1024px: Small screens, laptops
1025px — 1200px: Desktops, large screens
1201px and more —  Extra large screens, TV

Mobile (Portrait): 320px to 480px (e.g., standard smartphones).
Mobile (Landscape) / Tablets: 481px to 768px.
Tablets (Landscape) / Laptops: 769px to 1024px.
Desktops: 1025px to 1200px.
Large Screens/TVs: 1201px and above


/*Mobile devices*/
@media (min-width: 320) and ( max-width:480){



}