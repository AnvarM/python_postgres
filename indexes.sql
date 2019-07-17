CREATE INDEX received_by_date on users_messages(receiver_id asc, send_date desc);
CREATE INDEX sent_by_date on users_messages(sender_id asc, send_date desc);
CREATE INDEX senders on users_messages(sender_id asc);
CREATE INDEX receivers on users_messages(receiver_id asc);
CREATE INDEX send_dates on users_messages(send_date desc);