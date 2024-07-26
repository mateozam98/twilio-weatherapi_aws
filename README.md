<h2 align="center"> Proyecto envió de pronostico de lluvia en el móvil por SMS y Whatsapp</h2>
<em> Twilio - Python - AWS EC2  </em>

<h3>Herramientas utilizadas</h3>

<p>Este proyecto busca crear una forma sencilla y automatizada de recibir información del clima diariamente. Mediante un programa sencillo, se consultará cada día una API de clima gratuita y se extraerá la información para cad día. Esta información será enviada como un SMS a tú teléfono movil, utilizando el servicio de Twilio.</p>  

<ul>
  <li>Python</li>
  <li>Twilio</li>
  <li>AWS EC2</li>
  <li>API Weather</li>
</ul>
<hr/>

# DataFrame con datos del API weather:
![image](https://github.com/mateozam98/twilio-weatherapi_aws/assets/61571125/b91c2c4c-9323-4038-94a7-558908679244)
# Envío de pronostico de lluvia desde la instancia de AWS
<p> Cada día se ejecuta un script de Python que consume la API de clima y envía el pronóstico de lluvia de Valencia, España, al teléfono mediante SMS y WhatsApp. Este proceso automatizado asegura que la información meteorológica se reciba puntualmente y de manera eficiente.</p>

![image](https://github.com/mateozam98/twilio-weatherapi_aws/assets/61571125/830d383b-8388-420f-af64-0caa0fc50ab8)
<p>Se ha configurado una instancia Ubuntu en EC2 en AWS para ejecutar diariamente un script de Python. Este script no solo se encarga de obtener y procesar datos, sino que también registra cada ejecución, lo que facilita el monitoreo y análisis de su rendimiento a lo largo del tiempo.</p>

# Mensajes recibidos:
<h3>Whatsapp:</h3>

![image](https://github.com/mateozam98/twilio-weatherapi_aws/assets/61571125/3e6d3a82-8f1f-49ca-9ae7-ae57380f145b)

<h3>SMS:</h3>

![image](https://github.com/user-attachments/assets/689bc118-bbe1-4fb6-bdc9-174e97a42f9b)











