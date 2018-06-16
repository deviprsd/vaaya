package com.vaaya.shraavani.vaaya

import android.os.Bundle
import com.vaaya.shraavani.vaaya.master.VaayaActivity

class SplashActivity : VaayaActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        // setTheme(R.style.VaayaTheme_NoActionBar)
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_splash)
    }

    override fun onResume() {
        super.onResume()
        runController()
    }
}
