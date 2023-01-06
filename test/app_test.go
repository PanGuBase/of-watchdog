package test

import (
	"bytes"
	"io/ioutil"
	"net/http"
	"testing"
)

func TestApp(t *testing.T) {
	target := "http://127.0.0.1:8080"
	client := http.Client{}
	req, _ := http.NewRequest(http.MethodGet, target, bytes.NewReader([]byte("hello world")))
	resp, _ := client.Do(req)
	defer resp.Body.Close()
	data, _ := ioutil.ReadAll(resp.Body)
	println(string(data))
}
