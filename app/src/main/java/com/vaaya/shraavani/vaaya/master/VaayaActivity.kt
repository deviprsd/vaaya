package com.vaaya.shraavani.vaaya.master

import android.annotation.SuppressLint
import android.content.pm.ActivityInfo
import android.os.Bundle
import android.support.v7.app.AppCompatActivity
import android.transition.Slide

@SuppressLint("Registered")
open class VaayaActivity: AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        requestedOrientation = ActivityInfo.SCREEN_ORIENTATION_PORTRAIT

        val slide = Slide()
        slide.duration = 1000
        window.exitTransition = slide
        window.enterTransition = slide
    }
}