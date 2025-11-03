package com.exemplo.projeto.controller;

import com.exemplo.projeto.model.Usuario;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ResponseBody;

import java.util.List;

@Controller
public class ProjetoController {

    private List<Usuario> listarUsuarios() {
        return List.of(
                new Usuario(1L, "Ana Silva", "ana.silva@example.com", "+55 11 99999-0001"),
                new Usuario(2L, "Bruno Souza", "bruno.souza@example.com", "+55 11 99999-0002"),
                new Usuario(3L, "Carla Pereira", "carla.pereira@example.com", "+55 11 99999-0003"),
                new Usuario(4L, "Diego Lima", "diego.lima@example.com", "+55 11 99999-0004")
        );
    }

    @GetMapping("/projeto")
    public String paginaInicial() {
        return "index";
    }

    @GetMapping("/projeto/home")
    public String paginaHome() {
        return "home";
    }

    @GetMapping("/projeto/getAll")
    @ResponseBody
    public List<Usuario> obterUsuarios() {
        return listarUsuarios();
    }
}
