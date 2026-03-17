import os

import pymysql
import pymysql.cursors



class MySQLConnection:
    def __init__(self):
        self.host = os.getenv("MYSQL_HOST")
        self.port = 3306
        self.user = 'root'
        self.password = 'root'
        self.database = 'digital_hunter'
        self.conn = None

    def connect_to_db(self):
        if self.conn is None:
            self.conn = pymysql.connect(
                host='localhost',
                port=3306,
                user='root',
                password='root',
                database='digital_hunter'
            )
        return self.conn


    def get_all_high_priority(self):
        conn = self.connect_to_db()
        query = """
            SELECT entity_id, target_name, priority_level, movement_distance_km FROM targets
            WHERE priority_level in (1,2)
            AND movement_distance_km > 5
        """
        with conn.cursor(pymysql.cursors.DictCursor) as cur:
            cur.execute(query)
            results = cur.fetchall()
            return results

    def signal_type_count(self):
        conn = self.connect_to_db()
        query = """
                   SELECT signal_type, COUNT(*) AS total FROM intel_signals
                   GROUP BY signal_type
                   ORDER BY total DESC 
                """
        with conn.cursor(pymysql.cursors.DictCursor) as cur:
            cur.execute(query)
            results = cur.fetchall()
            return results

    def top_3_unknown_targets(self):
        conn = self.connect_to_db()
        query = """
                SELECT entity_id, COUNT(*) AS total FROM intel_signals
                WHERE priority_level = 99
                GROUP BY entity_id
                ORDER BY total DESC
                LIMIT 3
                """
        with conn.cursor(pymysql.cursors.DictCursor) as cur:
            cur.execute(query)
            results = cur.fetchall()
            return results

    def q4(self):
        conn = self.connect_to_db()
        query = """
                SELECT entity_id, HOUR(timestamp) AS hour FROM intel_signals
                GROUP BY entity_id, HOUR(timestamp)
                HAVING SUM(distance_from_last) = 0
                ORDER BY entity_id
                """
        with conn.cursor(pymysql.cursors.DictCursor) as cur:
            cur.execute(query)
            results = cur.fetchall()
            for result in results:
                print(result)