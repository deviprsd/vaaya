package com.vaaya.shraavani.vaaya.master

import android.app.Application
import com.crashlytics.android.Crashlytics
import io.fabric.sdk.android.Fabric
import io.realm.Realm
import io.realm.RealmConfiguration
import java.io.File
import java.util.*


class VaayaApplication: Application() {
    override fun onCreate() {
        super.onCreate()
        Realm.init(this)
        val realmConfiguration = RealmConfiguration.Builder()
                .name(getDatabaseName())
                .build()

        Realm.setDefaultConfiguration(realmConfiguration)
        Fabric.with(this, Crashlytics())
    }

    private fun getDatabaseName(): String {
        fun ClosedRange<Char>.randomString(lenght: Int) = (1..lenght).map {
            (Random().nextInt(endInclusive.toInt() - start.toInt()) + start.toInt()).toChar()
        }.joinToString("")

        val db = File(filesDir, "db.vaaya")
        var uuid = "vaaya.realm"

        return if(db.exists()) {
            db.bufferedReader().use { it.readLine() }
        } else {
            if(db.createNewFile()) {
                uuid = ('a'..'z').randomString(8) + ".realm"
                db.printWriter().use {
                    it.println(uuid)
                }
            }
            uuid
        }
    }
}