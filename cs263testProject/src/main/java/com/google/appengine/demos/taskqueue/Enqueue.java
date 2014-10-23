package com.google.appengine.demos.taskqueue;
// The Enqueue servlet should be mapped to the "/enqueue" URL.
import com.google.appengine.api.taskqueue.Queue;
import java.util.logging.Level;
import com.google.appengine.api.memcache.*;
import java.lang.Object;

import com.google.appengine.api.taskqueue.QueueFactory;
import static com.google.appengine.api.taskqueue.TaskOptions.Builder.*;

import java.io.IOException;
import java.util.Properties;
import javax.servlet.ServletException;

import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

public class Enqueue extends HttpServlet {
    protected void doPost(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        String key = request.getParameter("key");
        String value = request.getParameter("value");

        // Add the task to the default queue.
        Queue queue = QueueFactory.getDefaultQueue();
        queue.add(withUrl("/worker").param("key", key).param("value", value));
        //queue.add(withUrl("/worker").param("value", value));

        // response.sendRedirect("/done.html");
//        response.sendRedirect("/test");
        response.sendRedirect("/tqueue.jsp?key=" + key);
    }
}