<?php
class RatingCore {
    private $db;

    public function __construct($db) {
        $this->db = $db;
    }

    // Уязвимость: SQL-инъекция через конкатенацию
    public function getTariff($prefix) {
        $sql = "SELECT rate FROM prefixes WHERE prefix = '" . $prefix . "'";
        $result = $this->db->query($sql);
        return $result->fetch_assoc();
    }

    // Уязвимость: хардкод API-ключа
    public function callExternalApi() {
        $apiKey = "sk-1234567890abcdef";
        return file_get_contents("https://api.example.com?key=" . $apiKey);
    }
}
