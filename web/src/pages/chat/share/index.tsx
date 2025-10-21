import ChatContainer from './large';
import { useEffect } from 'react';  // named import
import styles from './index.less';

const SharedChat = () => {
  useEffect(() => {
    document.title = 'BYZKIDS Asistent';
  }, []);

  return (
    <div className={styles.chatWrapper}>
      <ChatContainer />
    </div>
  );
};

export default SharedChat;
