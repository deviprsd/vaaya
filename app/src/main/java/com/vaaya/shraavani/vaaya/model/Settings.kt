package com.vaaya.shraavani.vaaya.model

import io.realm.RealmObject
import io.realm.annotations.PrimaryKey

open class Settings: RealmObject() {
    @PrimaryKey var key: String? = null
    var settings: String? = null
}