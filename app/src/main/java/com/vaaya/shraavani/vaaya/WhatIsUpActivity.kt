package com.vaaya.shraavani.vaaya

import android.content.ClipData
import android.graphics.Color
import android.os.Bundle
import android.view.DragEvent
import android.view.MotionEvent
import android.view.ScaleGestureDetector
import android.view.View
import android.view.View.OnTouchListener
import android.widget.ImageView
import com.vaaya.shraavani.vaaya.master.VaayaActivity
import kotlinx.android.synthetic.main.activity_whatsup.*








class WhatIsUpActivity : VaayaActivity() {

    private lateinit var mScaleGestureDetector: ScaleGestureDetector
    private var mScaleFactor = 1.0f
    private var mScaleFactorMax = 0.0f

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_whatsup)

        vaaya_mood_anger.setColorFilter(Color.RED)
        vaaya_mood_joy.setColorFilter(Color.BLUE)
        vaaya_mood_sad.setColorFilter(Color.BLACK)
        vaaya_mood_disgust.setColorFilter(Color.GREEN)
        vaaya_mood_anxious.setColorFilter(Color.CYAN)

        vaaya_mood_anger.setOnTouchListener(MoodTouchListener())
        vaaya_mood_joy.setOnTouchListener(MoodTouchListener())
        vaaya_mood_sad.setOnTouchListener(MoodTouchListener())
        vaaya_mood_disgust.setOnTouchListener(MoodTouchListener())
        vaaya_mood_anxious.setOnTouchListener(MoodTouchListener())

        vaaya_mood_pool.setOnTouchListener { v: View, e: MotionEvent ->
            mScaleGestureDetector.onTouchEvent(e);
            return@setOnTouchListener true;
        }
        mScaleGestureDetector = ScaleGestureDetector(this, ScaleListener())

        vaaya_mood_pool_layout.setOnDragListener { v: View, e: DragEvent ->
            when (e.action) {
                DragEvent.ACTION_DRAG_STARTED -> {}
                DragEvent.ACTION_DRAG_ENTERED -> {
                    vaaya_mood_pool.setColorFilter(Color.BLACK)
                }
                DragEvent.ACTION_DRAG_EXITED -> {
                    vaaya_mood_pool.clearColorFilter()
                }
                DragEvent.ACTION_DROP -> {
                    val view = e.localState as ImageView
                    vaaya_mood_generic.colorFilter = view.colorFilter
                    if(vaaya_mood_generic.visibility == View.INVISIBLE) {
                        vaaya_mood_generic.visibility = View.VISIBLE
                    }

                    view.clearColorFilter()
                    view.isEnabled = false
                    view.visibility = View.VISIBLE
                }
                DragEvent.ACTION_DRAG_ENDED -> {
                    vaaya_mood_pool.clearColorFilter()
                    if(!e.result) {
                        (e.localState as View).visibility = View.VISIBLE
                    }
                }
                else -> {
                    return@setOnDragListener false
                }
            }
            return@setOnDragListener true
        }
    }

    private inner class MoodTouchListener : OnTouchListener {
        override fun onTouch(view: View, motionEvent: MotionEvent): Boolean {
            if (motionEvent.action == MotionEvent.ACTION_DOWN) {
                val data = ClipData.newPlainText("", "")
                val shadowBuilder = View.DragShadowBuilder(view)
                view.startDrag(data, shadowBuilder, view, 0)
                view.visibility = View.INVISIBLE
                return true
            } else {
                return false
            }
        }
    }

    private inner class ScaleListener : ScaleGestureDetector.SimpleOnScaleGestureListener() {
        override fun onScale(scaleGestureDetector: ScaleGestureDetector): Boolean {
            if(mScaleFactorMax == 0.0f) {
                mScaleFactorMax = (vaaya_mood_pool.width.toFloat() - convertDpToPixel(4.0f)) / vaaya_mood_generic.width
            }
            //Log.i("color", mScaleFactorMax.toString())
            mScaleFactor *= scaleGestureDetector.scaleFactor
            mScaleFactor = Math.max(0.1f, Math.min(mScaleFactor, mScaleFactorMax))
            vaaya_mood_generic.scaleX = mScaleFactor
            vaaya_mood_generic.scaleY = mScaleFactor
            return true
        }
    }
}
