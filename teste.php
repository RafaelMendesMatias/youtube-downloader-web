<?php

$url = $_GET['url'];

// Parâmetros a serem passados para o script Python

// Monta o comando para chamar o script Python
$command = ".\youtube_downloader_web\Scripts\activate && python main.py $url"; // Use o caminho correto para o Python, se necessário

// Executa o comando e aguarda a resposta
$output = [];
$return_var = 0;
exec($command, $output, $return_var);

// Exibe a saída do script Python
// foreach ($output as $line) {
    // echo $line . "<br>";
// }

// Verifica o código de retorno
if ($return_var !== 0) {
    echo "Erro ao executar o script Python.";
}
?>


<video width="850" height="475" controls autoplay muted>
  <source src="<?php echo $output[0]?>" type="video/mp4">
</video>